from django.dispatch import receiver
from django.contrib import messages
from django.contrib.auth.signals import user_logged_in, user_logged_out
from django.contrib.messages.api import MessageFailure


@receiver(user_logged_in)
def login_message(sender, request, user, **kwargs):
    try:
        messages.success(request, "You have logged in successfully.")
    except MessageFailure:
        pass


@receiver(user_logged_out)
def logout_message(sender, request, user, **kwargs):
    try:
        messages.success(request, "You have logged out successfully.")
    except MessageFailure:
        pass
