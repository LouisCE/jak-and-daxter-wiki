from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Collectable


class CollectableTests(TestCase):

    def setUp(self):
        # Users
        self.staff_user = User.objects.create_user(
            username="staff",
            password="pass",
            is_staff=True
        )
        self.regular_user = User.objects.create_user(
            username="user",
            password="pass"
        )

        # Collectables
        self.item = Collectable.objects.create(
            name="Precursor Orb",
            description="Shiny collectible",
            order=1
        )

        self.client = Client()

    # Public views
    def test_collectable_list_view_loads(self):
        response = self.client.get(reverse("collectable_list"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Precursor Orb")

    # Permissions
    def test_non_staff_cannot_access_create_view(self):
        self.client.login(username="user", password="pass")
        response = self.client.get(reverse("collectable_create"))
        self.assertEqual(response.status_code, 403)

    def test_staff_can_access_create_view(self):
        self.client.login(username="staff", password="pass")
        response = self.client.get(reverse("collectable_create"))
        self.assertEqual(response.status_code, 200)

    def test_non_staff_cannot_access_update_view(self):
        self.client.login(username="user", password="pass")
        response = self.client.get(reverse("collectable_update", args=[self.item.pk]))
        self.assertEqual(response.status_code, 403)

    def test_non_staff_cannot_access_delete_view(self):
        self.client.login(username="user", password="pass")
        response = self.client.get(reverse("collectable_delete", args=[self.item.pk]))
        self.assertEqual(response.status_code, 403)

    # CRUD
    def test_staff_can_create_collectable(self):
        self.client.login(username="staff", password="pass")
        response = self.client.post(reverse("collectable_create"), {
            "name": "Precursor Node",
            "description": "Another collectible"
        })
        self.assertTrue(Collectable.objects.filter(name="Precursor Node").exists())
        self.assertEqual(response.status_code, 302)

    def test_staff_can_update_collectable(self):
        self.client.login(username="staff", password="pass")
        response = self.client.post(reverse("collectable_update", args=[self.item.pk]), {
            "name": "Updated Orb",
            "description": self.item.description
        })
        self.item.refresh_from_db()
        self.assertEqual(self.item.name, "Updated Orb")
        self.assertEqual(response.status_code, 302)

    def test_staff_can_delete_collectable(self):
        self.client.login(username="staff", password="pass")
        response = self.client.post(reverse("collectable_delete", args=[self.item.pk]))
        self.assertFalse(Collectable.objects.filter(pk=self.item.pk).exists())
        self.assertEqual(response.status_code, 302)

    # Model behaviour
    def test_collectable_string_representation(self):
        self.assertEqual(str(self.item), "Precursor Orb")

    def test_collectable_ordering(self):
        c2 = Collectable.objects.create(name="Precursor Node", order=0)
        items = list(Collectable.objects.all())
        self.assertEqual(items[0], c2)
