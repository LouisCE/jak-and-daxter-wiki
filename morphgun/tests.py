from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Weapon, Colour, WeaponRating


class MorphGunTests(TestCase):

    def setUp(self):
        # Create users
        self.staff_user = User.objects.create_user(username='staff', password='pass', is_staff=True)
        self.regular_user = User.objects.create_user(username='user', password='pass')

        # Create Colour
        self.colour = Colour.objects.create(name="Red", description="Test Colour")

        # Create Weapon
        self.weapon = Weapon.objects.create(name="Test Gun", colour=self.colour, description="Test Weapon")

        # Client
        self.client = Client()

    # Permissions
    def test_non_staff_cannot_access_create_weapon(self):
        self.client.login(username='user', password='pass')
        response = self.client.get(reverse('create_weapon'))
        self.assertEqual(response.status_code, 302)  # Redirects due to @user_passes_test

    def test_staff_can_access_create_weapon(self):
        self.client.login(username='staff', password='pass')
        response = self.client.get(reverse('create_weapon'))
        self.assertEqual(response.status_code, 200)

    def test_login_required_rate_weapons(self):
        response = self.client.get(reverse('rate_weapons'))
        self.assertEqual(response.status_code, 302)  # Should redirect to login

    # CRUD
    def test_create_weapon(self):
        self.client.login(username='staff', password='pass')
        response = self.client.post(reverse('create_weapon'), {
            'name': 'New Gun',
            'colour': self.colour.id,
            'description': 'Description',
        })
        self.assertTrue(Weapon.objects.filter(name='New Gun').exists())
        self.assertEqual(response.status_code, 302)  # Redirect to detail

    def test_update_weapon(self):
        self.client.login(username='staff', password='pass')
        response = self.client.post(reverse('update_weapon', args=[self.weapon.pk]), {
            'name': 'Updated Gun',
            'colour': self.colour.id,
            'description': 'Updated Description',
        })
        self.weapon.refresh_from_db()
        self.assertEqual(self.weapon.name, 'Updated Gun')
        self.assertEqual(response.status_code, 302)

    def test_delete_weapon(self):
        self.client.login(username='staff', password='pass')
        response = self.client.post(reverse('delete_weapon', args=[self.weapon.pk]))
        self.assertFalse(Weapon.objects.filter(pk=self.weapon.pk).exists())
        self.assertEqual(response.status_code, 302)

    # Rate Weapons
    def test_rate_weapons_creates_rating(self):
        self.client.login(username='user', password='pass')
        response = self.client.post(reverse('rate_weapons'), {
            f'weapon_{self.weapon.id}': 7
        })
        self.assertTrue(WeaponRating.objects.filter(user=self.regular_user, weapon=self.weapon).exists())
        self.assertEqual(response.status_code, 200)

    def test_rate_weapons_incomplete_submission(self):
        self.client.login(username='user', password='pass')
        response = self.client.post(reverse('rate_weapons'), {})  # Missing rating
        self.assertFalse(WeaponRating.objects.filter(user=self.regular_user).exists())
        self.assertEqual(response.status_code, 302)  # Redirect due to error message
