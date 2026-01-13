from django.dispatch import receiver
from django.contrib import messages
from django.contrib.auth.signals import user_logged_in, user_logged_out


@receiver(user_logged_in)
def login_message(sender, request, user, **kwargs):
    messages.success(request, "You have logged in successfully.")


@receiver(user_logged_out)
def logout_message(sender, request, user, **kwargs):
    messages.success(request, "You have logged out successfully.")
