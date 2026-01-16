from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model

from home.forms import CustomUserCreationForm


User = get_user_model()


class HomeTests(TestCase):
    """
    Tests for Home app (views).

    Focus:
    - index loads correctly
    - register loads + creates a user on valid POST (using the *real* form fields)
    - invalid register does not create a user
    - logout redirects correctly

    Notes:
    - Avoid asserting exact page copy (templates can change).
    - Assert templates / status codes / redirects and DB side effects instead.
    """

    def _build_valid_register_payload(self, username="newuser"):
        """
        Build a POST payload that matches your CustomUserCreationForm fields.
        This prevents tests from breaking if the form requires extra fields
        (e.g. email).
        """
        form = CustomUserCreationForm()

        payload = {}
        for name, field in form.fields.items():
            # Handle common expected fields
            if name == "username":
                payload[name] = username
                continue

            if name == "password1":
                payload[name] = "StrongPassword123!"
                continue

            if name == "password2":
                payload[name] = "StrongPassword123!"
                continue

            if name == "email":
                payload[name] = f"{username}@example.com"
                continue

            # Best-effort defaults for any other required fields
            if field.required:
                # If it has choices, pick the first valid choice value
                if getattr(field, "choices", None):
                    # choices may include a blank option - pick first non-blank if possible
                    choices = [c for c in field.choices if c[0] not in ("", None)]
                    payload[name] = choices[0][0] if choices else field.choices[0][0]
                else:
                    payload[name] = "test"

        return payload

    def test_index_view_loads(self):
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "home/index.html")

    def test_register_view_get(self):
        response = self.client.get(reverse("register"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "home/register.html")
        self.assertIn("form", response.context)

    def test_register_view_post_creates_user(self):
        payload = self._build_valid_register_payload(username="newuser")
        response = self.client.post(reverse("register"), payload)

        # On success it should redirect to login
        if response.status_code != 302:
            # Surface form errors to make diagnosis instant
            form = response.context.get("form")
            errors = form.errors.as_text() if form else "No form in context"
            self.fail(
                f"Register did not redirect. Status={response.status_code}.\n"
                f"Payload keys={sorted(payload.keys())}\n"
                f"Form errors:\n{errors}"
            )

        self.assertTrue(User.objects.filter(username="newuser").exists())

    def test_register_view_post_invalid_data(self):
        # Intentionally invalid: password mismatch
        payload = self._build_valid_register_payload(username="baduser")
        payload["password1"] = "StrongPassword123!"
        payload["password2"] = "DifferentPassword123!"

        response = self.client.post(reverse("register"), payload)

        # Should re-render the register page with errors
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "home/register.html")
        self.assertFalse(User.objects.filter(username="baduser").exists())

    def test_logout_view_redirects_home(self):
        User.objects.create_user(username="u", password="pass")
        self.client.login(username="u", password="pass")

        response = self.client.get(reverse("logout"))
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response.url, reverse("home"))
