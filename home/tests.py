from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User

class HomeTests(TestCase):

    def setUp(self):
        self.client = Client()

    # Public view
    def test_index_view_loads(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Welcome to the Jak and Daxter Wiki")

    # Registration view GET
    def test_register_view_get(self):
        response = self.client.get(reverse('register'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "<form")

    # Registration view POST creates user
    def test_register_view_post_creates_user(self):
        form_data = {
            'username': 'testuser',
            'email': 'test@example.com',
            'password1': 'StrongPass123!',
            'password2': 'StrongPass123!'
        }
        response = self.client.post(reverse('register'), form_data)
        self.assertRedirects(response, reverse('login'))
        self.assertTrue(User.objects.filter(username='testuser').exists())

    # Registration view POST with invalid data does not create user
    def test_register_view_post_invalid_data(self):
        form_data = {
            'username': '', # Missing username
            'email': 'bademail',
            'password1': '123',
            'password2': '456'
        }
        response = self.client.post(reverse('register'), form_data)
        self.assertEqual(response.status_code, 200) # Form is re-rendered
        self.assertFalse(User.objects.filter(email='bademail').exists())
        self.assertContains(response, "<form")
