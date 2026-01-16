# morphgun/tests.py
from django.contrib.auth.models import User
from django.contrib.auth.signals import user_logged_in, user_logged_out
from django.db import IntegrityError
from django.test import TestCase
from django.urls import reverse

from morphgun.models import Colour, MorphGunUpgrade, Weapon, WeaponRating


class MorphGunTests(TestCase):
    """
    Unit tests for the Morph Gun app (models + views).

    Your project uses login/logout signals that add Django messages.
    In some test contexts those receivers can cause MessageFailure.
    We disconnect them here to keep tests stable.
    """

    @classmethod
    def setUpClass(cls):
        super().setUpClass()

        # Disconnect message-adding auth signal receivers (if present)
        try:
            from home import signals as home_signals

            cls._home_signals = home_signals
            user_logged_in.disconnect(home_signals.login_message)
            user_logged_out.disconnect(home_signals.logout_message)
        except Exception:
            cls._home_signals = None

    @classmethod
    def tearDownClass(cls):
        # Reconnect the receivers after tests complete
        if getattr(cls, "_home_signals", None):
            user_logged_in.connect(
                cls._home_signals.login_message,
                weak=False,
            )
            user_logged_out.connect(
                cls._home_signals.logout_message,
                weak=False,
            )
        super().tearDownClass()

    def setUp(self):
        # Users
        self.staff = User.objects.create_user(
            username="staff",
            password="pass",
            is_staff=True,
        )
        self.user = User.objects.create_user(
            username="user",
            password="pass",
            is_staff=False,
        )

        # Core data
        self.colour = Colour.objects.create(
            name="Red Eco",
            description="Red eco for weapon mods.",
            hex_code="#ff0000",
            order=1,
            image="placeholder",
        )
        self.weapon1 = Weapon.objects.create(
            name="Blaster",
            colour=self.colour,
            description="A rapid-fire weapon.",
            order=1,
            image="placeholder",
        )
        self.weapon2 = Weapon.objects.create(
            name="Beam Reflexor",
            colour=self.colour,
            description="A precision beam weapon.",
            order=2,
            image="placeholder",
        )

        # Upgrades
        self.upgrade_jak2 = MorphGunUpgrade.objects.create(
            name="Jak II Upgrade",
            game=MorphGunUpgrade.JAK_II,
            effect="Improves performance.",
            requirement="Story progress",
        )
        self.upgrade_jak2.weapons.add(self.weapon1)

        self.upgrade_jak3 = MorphGunUpgrade.objects.create(
            name="Jak 3 Upgrade",
            game=MorphGunUpgrade.JAK_III,
            effect="Adds an enhancement.",
            requirement="Complete challenge",
            price=25,
        )
        self.upgrade_jak3.weapons.add(self.weapon1)

    # -------------------------
    # Model tests
    # -------------------------
    def test_colour_str(self):
        self.assertEqual(str(self.colour), "Red Eco")

    def test_weapon_str(self):
        self.assertEqual(str(self.weapon1), "Blaster")

    def test_weapon_rating_str(self):
        rating = WeaponRating.objects.create(
            user=self.user,
            weapon=self.weapon1,
            score=8,
        )
        self.assertIn("Blaster", str(rating))
        self.assertIn("8/10", str(rating))
        self.assertIn("user", str(rating))

    def test_upgrade_str(self):
        self.assertEqual(
            str(self.upgrade_jak2),
            "Jak II Upgrade (Jak II)",
        )

    def test_weapon_rating_unique_together(self):
        WeaponRating.objects.create(
            user=self.user,
            weapon=self.weapon1,
            score=7,
        )
        with self.assertRaises(IntegrityError):
            WeaponRating.objects.create(
                user=self.user,
                weapon=self.weapon1,
                score=9,
            )

    # -------------------------
    # View tests (public pages)
    # -------------------------
    def test_weapon_list_loads(self):
        url = reverse("weapon_list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

        self.assertIn("weapons_by_colour", response.context)
        groups = response.context["weapons_by_colour"]
        self.assertTrue(len(groups) >= 1)
        self.assertEqual(groups[0]["grouper"], self.colour)

    def test_weapon_detail_loads_and_splits_upgrades(self):
        url = reverse(
            "weapon_detail",
            kwargs={"pk": self.weapon1.pk},
        )
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

        self.assertIn("jak2_upgrades", response.context)
        self.assertIn("jak3_upgrades", response.context)
        self.assertIn(
            self.upgrade_jak2,
            response.context["jak2_upgrades"],
        )
        self.assertIn(
            self.upgrade_jak3,
            response.context["jak3_upgrades"],
        )

    # -------------------------
    # Weapon CRUD permissions
    # -------------------------
    def test_non_staff_cannot_access_create_weapon(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse("create_weapon"))
        self.assertEqual(response.status_code, 403)

    def test_staff_can_create_weapon(self):
        self.client.force_login(self.staff)
        response = self.client.post(
            reverse("create_weapon"),
            {
                "name": "Vulcan Fury",
                "colour": self.colour.pk,
                "description": "Heavy weapon.",
                "order": 3,
                "image": "placeholder",
            },
        )
        # create_weapon redirects to weapon_detail(pk=created.pk)
        self.assertEqual(response.status_code, 302)

        created = Weapon.objects.get(name="Vulcan Fury")
        self.assertEqual(created.colour, self.colour)
        self.assertEqual(
            response.url,
            reverse(
                "weapon_detail",
                kwargs={"pk": created.pk},
            ),
        )

    def test_staff_can_update_weapon(self):
        self.client.force_login(self.staff)
        response = self.client.post(
            reverse(
                "update_weapon",
                kwargs={"pk": self.weapon1.pk},
            ),
            {
                "name": "Blaster (Updated)",
                "colour": self.colour.pk,
                "description": "Updated description.",
                "order": 1,
                "image": "placeholder",
            },
        )
        self.assertEqual(response.status_code, 302)
        self.assertEqual(
            response.url,
            reverse(
                "weapon_detail",
                kwargs={"pk": self.weapon1.pk},
            ),
        )

        self.weapon1.refresh_from_db()
        self.assertEqual(self.weapon1.name, "Blaster (Updated)")

    def test_staff_can_delete_weapon(self):
        self.client.force_login(self.staff)
        response = self.client.post(
            reverse(
                "delete_weapon",
                kwargs={"pk": self.weapon2.pk},
            )
        )
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, reverse("weapon_list"))
        self.assertFalse(
            Weapon.objects.filter(pk=self.weapon2.pk).exists()
        )

    # -------------------------
    # Colour CRUD permissions
    # -------------------------
    def test_non_staff_cannot_create_colour(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse("colour_create"))
        self.assertEqual(response.status_code, 403)

    def test_staff_can_create_colour(self):
        self.client.force_login(self.staff)
        response = self.client.post(
            reverse("colour_create"),
            {
                "name": "Blue Eco",
                "description": "Blue eco colour.",
                "hex_code": "#00ffff",
                "order": 2,
                "image": "placeholder",
            },
        )
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, reverse("weapon_list"))
        self.assertTrue(
            Colour.objects.filter(name="Blue Eco").exists()
        )

    def test_staff_can_update_colour(self):
        self.client.force_login(self.staff)
        response = self.client.post(
            reverse(
                "colour_update",
                kwargs={"pk": self.colour.pk},
            ),
            {
                "name": "Red Eco (Updated)",
                "description": "Updated description.",
                "hex_code": "#ff0000",
                "order": 1,
                "image": "placeholder",
            },
        )
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, reverse("weapon_list"))

        self.colour.refresh_from_db()
        self.assertEqual(self.colour.name, "Red Eco (Updated)")

    def test_staff_can_delete_colour(self):
        extra_colour = Colour.objects.create(
            name="Temp Colour",
            description="Temporary.",
            hex_code="#ffffff",
            order=99,
            image="placeholder",
        )
        self.client.force_login(self.staff)
        response = self.client.post(
            reverse(
                "colour_delete",
                kwargs={"pk": extra_colour.pk},
            )
        )
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, reverse("weapon_list"))
        self.assertFalse(
            Colour.objects.filter(pk=extra_colour.pk).exists()
        )

    # -------------------------
    # Upgrade CRUD permissions
    # -------------------------
    def test_non_staff_cannot_access_upgrade_views(self):
        self.client.force_login(self.user)
        self.assertEqual(
            self.client.get(reverse("create_upgrade")).status_code,
            403,
        )
        self.assertEqual(
            self.client.get(
                reverse(
                    "update_upgrade",
                    kwargs={"pk": self.upgrade_jak2.pk},
                )
            ).status_code,
            403,
        )
        self.assertEqual(
            self.client.get(
                reverse(
                    "delete_upgrade",
                    kwargs={"pk": self.upgrade_jak2.pk},
                )
            ).status_code,
            403,
        )

    def test_staff_can_create_upgrade_redirects_to_weapon_detail(self):
        self.client.force_login(self.staff)
        response = self.client.post(
            reverse("create_upgrade"),
            {
                "name": "New Upgrade",
                "game": MorphGunUpgrade.JAK_II,
                "effect": "Does something useful.",
                "requirement": "Complete mission",
                "price": "",
                "weapons": [self.weapon1.pk],
            },
        )
        self.assertEqual(response.status_code, 302)
        self.assertTrue(
            MorphGunUpgrade.objects.filter(name="New Upgrade").exists()
        )

        created = MorphGunUpgrade.objects.get(name="New Upgrade")
        self.assertEqual(
            response.url,
            reverse(
                "weapon_detail",
                kwargs={"pk": created.weapons.first().pk},
            ),
        )

    def test_staff_can_update_upgrade_redirects_to_weapon_detail(self):
        self.client.force_login(self.staff)
        response = self.client.post(
            reverse(
                "update_upgrade",
                kwargs={"pk": self.upgrade_jak2.pk},
            ),
            {
                "name": "Jak II Upgrade (Updated)",
                "game": MorphGunUpgrade.JAK_II,
                "effect": "Updated effect.",
                "requirement": "Updated requirement",
                "price": "",
                "weapons": [self.weapon1.pk],
            },
        )
        self.assertEqual(response.status_code, 302)
        self.assertEqual(
            response.url,
            reverse(
                "weapon_detail",
                kwargs={"pk": self.weapon1.pk},
            ),
        )

        self.upgrade_jak2.refresh_from_db()
        self.assertEqual(
            self.upgrade_jak2.name,
            "Jak II Upgrade (Updated)",
        )

    def test_staff_can_delete_upgrade_redirects_to_weapon_detail(self):
        self.client.force_login(self.staff)
        pk = self.upgrade_jak3.pk
        response = self.client.post(
            reverse(
                "delete_upgrade",
                kwargs={"pk": pk},
            )
        )
        self.assertEqual(response.status_code, 302)
        # upgrade_jak3 was attached to weapon1, so should redirect there
        self.assertEqual(
            response.url,
            reverse(
                "weapon_detail",
                kwargs={"pk": self.weapon1.pk},
            ),
        )
        self.assertFalse(MorphGunUpgrade.objects.filter(pk=pk).exists())

    # -------------------------
    # Rating + rankings
    # -------------------------
    def test_rate_weapons_requires_login(self):
        response = self.client.get(reverse("rate_weapons"))
        self.assertIn(response.status_code, (301, 302))

    def test_rate_weapons_incomplete_submission_saves_partial_then_redirects(
        self,
    ):
        """
        IMPORTANT: Your current view saves ratings as it loops.
        If you submit a score for weapon1 but omit weapon2, it will
        save weapon1 then redirect when it hits the missing weapon2.
        """
        self.client.force_login(self.user)

        response = self.client.post(
            reverse("rate_weapons"),
            {
                f"weapon_{self.weapon1.pk}": "7",
                # weapon2 missing -> triggers error + redirect
            },
        )
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, reverse("rate_weapons"))

        # weapon1 rating was created before the redirect
        self.assertEqual(
            WeaponRating.objects.filter(user=self.user).count(),
            1,
        )
        self.assertTrue(
            WeaponRating.objects.filter(
                user=self.user,
                weapon=self.weapon1,
                score=7,
            ).exists()
        )

    def test_rate_weapons_complete_submission_creates_ratings(self):
        self.client.force_login(self.user)

        response = self.client.post(
            reverse("rate_weapons"),
            {
                f"weapon_{self.weapon1.pk}": "7",
                f"weapon_{self.weapon2.pk}": "9",
            },
        )
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, reverse("weapon_rankings"))
        self.assertEqual(
            WeaponRating.objects.filter(user=self.user).count(),
            2,
        )

    def test_weapon_rankings_no_user_ratings_shows_no_change(self):
        self.client.force_login(self.user)

        other = User.objects.create_user(
            username="other",
            password="pass",
        )
        WeaponRating.objects.create(
            user=other,
            weapon=self.weapon1,
            score=5,
        )
        WeaponRating.objects.create(
            user=other,
            weapon=self.weapon2,
            score=6,
        )

        response = self.client.get(reverse("weapon_rankings"))
        self.assertEqual(response.status_code, 200)

        community = response.context["community_rankings"]
        for weapon in community:
            self.assertIsNone(weapon.rank_change)
            self.assertIsNone(weapon.rank_change_abs)

    def test_weapon_rankings_with_user_ratings_calculates_change(self):
        self.client.force_login(self.user)

        other = User.objects.create_user(
            username="other2",
            password="pass",
        )
        WeaponRating.objects.create(
            user=other,
            weapon=self.weapon1,
            score=5,
        )
        WeaponRating.objects.create(
            user=other,
            weapon=self.weapon2,
            score=6,
        )

        WeaponRating.objects.create(
            user=self.user,
            weapon=self.weapon1,
            score=10,
        )
        WeaponRating.objects.create(
            user=self.user,
            weapon=self.weapon2,
            score=1,
        )

        response = self.client.get(reverse("weapon_rankings"))
        self.assertEqual(response.status_code, 200)

        community = response.context["community_rankings"]
        for weapon in community:
            self.assertIsNotNone(weapon.rank_change)
            self.assertIsNotNone(weapon.rank_change_abs)
            self.assertIsInstance(weapon.rank_change_abs, int)
