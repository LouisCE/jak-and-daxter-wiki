from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth.views import LoginView

from .forms import CustomUserCreationForm


def index(request):
    return render(request, "home/index.html")


def register(request):
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                request,
                "Account created successfully. You can now log in."
            )
            return redirect("login")
    else:
        form = CustomUserCreationForm()

    return render(
        request,
        "home/register.html",
        {"form": form}
    )


class CustomLoginView(LoginView):
    """
    Extends Django's built-in LoginView to provide
    user feedback on successful login.
    """
    template_name = "home/login.html"

    def form_valid(self, form):
        messages.success(
            self.request,
            "You have logged in successfully."
        )
        return super().form_valid(form)


def logout_view(request):
    """
    Logs the user out and provides feedback.
    """
    logout(request)
    messages.success(
        request,
        "You have logged out successfully."
    )
    return redirect("home")
