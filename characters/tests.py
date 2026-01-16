from django.contrib.auth.models import User
from django.contrib.auth.signals import user_logged_in, user_logged_out
from django.test import TestCase
from django.urls import reverse

from characters.models import Character


class CharacterTests(TestCase):
    """
    Tests for Characters app (models + CBV permissions + CRUD).

    Notes:
    - This project uses login/logout signals in home/signals.py that add Django
      messages. Django's test client .login() can trigger those signals with a
      request object that may not have the messages framework attached in some
      contexts.
    - To keep tests stable without changing production logic, we disconnect
      those receivers during this test module and reconnect afterwards.
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

        # Character (existing)
        self.character = Character.objects.create(
            name="Jak",
            quote="I'm going to save the world.",
            image="placeholder",
            sex="Male",
            age="18",
            skin="Tan",
            hair="Blond",
            eyes="Blue",
            height="5'8",
            weight="70kg",
            occupation="Hero",
            appearance="Athletic and determined.",
            personality="Brave and loyal.",
            order=1,
        )

    # -------------------------
    # Model tests
    # -------------------------
    def test_character_string_representation(self):
        self.assertEqual(str(self.character), "Jak")

    def test_character_ordering(self):
        Character.objects.create(
            name="Daxter",
            quote="I'm the outrider!",
            image="placeholder",
            sex="Male",
            age="18",
            skin="Orange",
            hair="N/A",
            eyes="Green",
            height="2'0",
            weight="15kg",
            occupation="Sidekick",
            appearance="Small ottsel.",
            personality="Funny and cocky.",
            order=0,
        )
        qs = list(Character.objects.all())
        self.assertEqual(qs[0].name, "Daxter")
        self.assertEqual(qs[1].name, "Jak")

    # -------------------------
    # View tests (public pages)
    # -------------------------
    def test_character_list_view_loads(self):
        response = self.client.get(reverse("character_list"))
        self.assertEqual(response.status_code, 200)
        self.assertIn("characters", response.context)
        self.assertContains(response, "Jak")

    def test_character_detail_view_loads(self):
        response = self.client.get(
            reverse(
                "character_detail",
                kwargs={"pk": self.character.pk},
            )
        )
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Jak")

    # -------------------------
    # Permission tests
    # -------------------------
    def test_login_required_for_create(self):
        response = self.client.get(reverse("character_create"))
        self.assertEqual(response.status_code, 302)  # redirects to login

    def test_login_required_for_update(self):
        response = self.client.get(
            reverse(
                "character_update",
                kwargs={"pk": self.character.pk},
            )
        )
        self.assertEqual(response.status_code, 302)  # redirects to login

    def test_non_staff_cannot_access_create_view(self):
        self.client.login(username="user", password="pass")
        response = self.client.get(reverse("character_create"))
        self.assertEqual(response.status_code, 403)

    def test_staff_can_access_create_view(self):
        self.client.login(username="staff", password="pass")
        response = self.client.get(reverse("character_create"))
        self.assertEqual(response.status_code, 200)

    # -------------------------
    # CRUD tests (staff only)
    # -------------------------
    def test_staff_can_create_character(self):
        self.client.login(username="staff", password="pass")

        response = self.client.post(
            reverse("character_create"),
            {
                "name": "Daxter",
                "quote": "I'm the hero here!",
                "image": "placeholder",
                "sex": "Male",
                "age": "18",
                "skin": "Orange",
                "hair": "N/A",
                "eyes": "Green",
                "height": "2'0",
                "weight": "15kg",
                "occupation": "Sidekick",
                "appearance": "Small ottsel.",
                "personality": "Funny and cocky.",
                "order": 2,
            },
        )

        # Success url is character_list
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse("character_list"))
        self.assertTrue(
            Character.objects.filter(name="Daxter").exists()
        )

    def test_staff_can_update_character(self):
        self.client.login(username="staff", password="pass")

        response = self.client.post(
            reverse(
                "character_update",
                kwargs={"pk": self.character.pk},
            ),
            {
                "name": "Jak Updated",
                "quote": self.character.quote,
                "image": "placeholder",
                "sex": self.character.sex,
                "age": self.character.age,
                "skin": self.character.skin,
                "hair": self.character.hair,
                "eyes": self.character.eyes,
                "height": self.character.height,
                "weight": self.character.weight,
                "occupation": self.character.occupation,
                "appearance": self.character.appearance,
                "personality": self.character.personality,
                "order": self.character.order,
            },
        )

        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse("character_list"))

        self.character.refresh_from_db()
        self.assertEqual(self.character.name, "Jak Updated")

    def test_staff_can_delete_character(self):
        self.client.login(username="staff", password="pass")
        response = self.client.post(
            reverse(
                "character_delete",
                kwargs={"pk": self.character.pk},
            )
        )
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse("character_list"))
        self.assertFalse(
            Character.objects.filter(pk=self.character.pk).exists()
        )
