from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Character


class CharacterTests(TestCase):

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

        # Characters
        self.character = Character.objects.create(
            name="Jak",
            quote="I'm gonna find my father.",
            order=1
        )

        self.client = Client()

    # Public views
    def test_character_list_view_loads(self):
        response = self.client.get(reverse("character_list"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Jak")

    def test_character_detail_view_loads(self):
        response = self.client.get(
            reverse("character_detail", args=[self.character.pk])
        )
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.character.name)

    # Permissions
    def test_non_staff_cannot_access_create_view(self):
        self.client.login(username="user", password="pass")
        response = self.client.get(reverse("character_create"))
        self.assertEqual(response.status_code, 403)

    def test_staff_can_access_create_view(self):
        self.client.login(username="staff", password="pass")
        response = self.client.get(reverse("character_create"))
        self.assertEqual(response.status_code, 200)

    def test_login_required_for_update(self):
        response = self.client.get(
            reverse("character_update", args=[self.character.pk])
        )
        self.assertEqual(response.status_code, 302)

    # CRUD
    def test_staff_can_create_character(self):
        self.client.login(username="staff", password="pass")
        response = self.client.post(reverse("character_create"), {
            "name": "Daxter",
            "quote": "Hey! I'm the real hero here. You can call me..."
            "Orange Lightning. Zazaziing!",
            "order": 2
        })
        self.assertTrue(Character.objects.filter(name="Daxter").exists())
        self.assertEqual(response.status_code, 302)

    def test_staff_can_update_character(self):
        self.client.login(username="staff", password="pass")
        response = self.client.post(
            reverse("character_update", args=[self.character.pk]),
            {
                "name": "Jak Updated",
                "quote": self.character.quote,
                "order": 1
            }
        )
        self.character.refresh_from_db()
        self.assertEqual(self.character.name, "Jak Updated")
        self.assertEqual(response.status_code, 302)

    def test_staff_can_delete_character(self):
        self.client.login(username="staff", password="pass")
        response = self.client.post(
            reverse("character_delete", args=[self.character.pk])
        )
        self.assertFalse(
            Character.objects.filter(pk=self.character.pk).exists()
        )
        self.assertEqual(response.status_code, 302)

    # Model behaviour
    def test_character_string_representation(self):
        self.assertEqual(str(self.character), "Jak")

    def test_character_ordering(self):
        c2 = Character.objects.create(name="Samos", order=0)
        characters = list(Character.objects.all())
        self.assertEqual(characters[0], c2)
