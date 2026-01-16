from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from django.contrib.auth.signals import user_logged_in, user_logged_out

from collectables.models import Collectable


class CollectableTests(TestCase):
    """
    Tests for Collectables app (models + views).

    NOTE:
    This project uses login/logout signals that add Django messages.
    The Django test client login can trigger those signals using a request
    that may not have messages attached in some contexts.
    To keep tests stable, we temporarily disconnect those receivers.
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
            user_logged_in.connect(cls._home_signals.login_message, weak=False)
            user_logged_out.connect(cls._home_signals.logout_message, weak=False)

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

        # Collectables (ensure ordering can be tested)
        self.item1 = Collectable.objects.create(
            name="Precursor Orb",
            description="A shiny orb.",
            image="placeholder",
            order=2,
        )
        self.item2 = Collectable.objects.create(
            name="Metal Head Skull Gem",
            description="A rare gem.",
            image="placeholder",
            order=1,
        )

    # -------------------------
    # Model tests
    # -------------------------
    def test_collectable_string_representation(self):
        self.assertEqual(str(self.item1), "Precursor Orb")

    def test_collectable_ordering(self):
        # Meta ordering is by 'order' (ascending)
        items = list(Collectable.objects.all())
        self.assertEqual(items[0], self.item2)
        self.assertEqual(items[1], self.item1)

    # -------------------------
    # View tests (public)
    # -------------------------
    def test_collectable_list_view_loads(self):
        response = self.client.get(reverse("collectable_list"))
        self.assertEqual(response.status_code, 200)
        self.assertIn("items", response.context)

        items = list(response.context["items"])
        # View orders by order, then name
        self.assertEqual(items[0], self.item2)
        self.assertEqual(items[1], self.item1)

    # -------------------------
    # Permissions (non-staff)
    # -------------------------
    def test_non_staff_cannot_access_create_view(self):
        self.client.login(username="user", password="pass")
        response = self.client.get(reverse("collectable_create"))
        self.assertEqual(response.status_code, 403)

    def test_non_staff_cannot_access_update_view(self):
        self.client.login(username="user", password="pass")
        response = self.client.get(reverse("collectable_update", kwargs={"pk": self.item1.pk}))
        self.assertEqual(response.status_code, 403)

    def test_non_staff_cannot_access_delete_view(self):
        self.client.login(username="user", password="pass")
        response = self.client.get(reverse("collectable_delete", kwargs={"pk": self.item1.pk}))
        self.assertEqual(response.status_code, 403)

    # -------------------------
    # Staff CRUD
    # -------------------------
    def test_staff_can_access_create_view(self):
        self.client.login(username="staff", password="pass")
        response = self.client.get(reverse("collectable_create"))
        self.assertEqual(response.status_code, 200)

    def test_staff_can_create_collectable(self):
        self.client.login(username="staff", password="pass")
        response = self.client.post(
            reverse("collectable_create"),
            {
                "name": "Eco Crystal",
                "description": "A crystal of eco energy.",
                "order": 3,
                "image": "placeholder",
            },
        )
        self.assertEqual(response.status_code, 302)
        self.assertTrue(Collectable.objects.filter(name="Eco Crystal").exists())

    def test_staff_can_update_collectable(self):
        self.client.login(username="staff", password="pass")
        response = self.client.post(
            reverse("collectable_update", kwargs={"pk": self.item1.pk}),
            {
                "name": "Updated Orb",
                "description": "Updated description.",
                "order": 2,
                "image": "placeholder",
            },
        )
        self.assertEqual(response.status_code, 302)

        self.item1.refresh_from_db()
        self.assertEqual(self.item1.name, "Updated Orb")

    def test_staff_can_delete_collectable(self):
        self.client.login(username="staff", password="pass")
        response = self.client.post(reverse("collectable_delete", kwargs={"pk": self.item2.pk}))
        self.assertEqual(response.status_code, 302)
        self.assertFalse(Collectable.objects.filter(pk=self.item2.pk).exists())
