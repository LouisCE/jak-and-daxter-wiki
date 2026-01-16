from django.contrib import messages
from django.contrib.auth.mixins import (
    LoginRequiredMixin,
    UserPassesTestMixin,
)
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    DeleteView,
    DetailView,
    ListView,
    UpdateView,
)

from .models import Character


class CharacterList(ListView):
    model = Character
    template_name = "characters/character_list.html"
    context_object_name = "characters"


class CharacterDetail(DetailView):
    model = Character
    template_name = "characters/character_detail.html"


class CharacterCreate(
    LoginRequiredMixin,
    UserPassesTestMixin,
    CreateView,
):
    model = Character
    fields = "__all__"
    template_name = "characters/character_form.html"
    success_url = reverse_lazy("character_list")

    def test_func(self):
        return self.request.user.is_staff

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(
            self.request,
            (
                f'Character "{self.object.name}" '
                "created successfully."
            ),
        )
        return response


class CharacterUpdate(
    LoginRequiredMixin,
    UserPassesTestMixin,
    UpdateView,
):
    model = Character
    fields = "__all__"
    template_name = "characters/character_form.html"
    success_url = reverse_lazy("character_list")

    def test_func(self):
        return self.request.user.is_staff

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(
            self.request,
            (
                f'Character "{self.object.name}" '
                "updated successfully."
            ),
        )
        return response


class CharacterDelete(
    LoginRequiredMixin,
    UserPassesTestMixin,
    DeleteView,
):
    model = Character
    template_name = "characters/character_confirm_delete.html"
    success_url = reverse_lazy("character_list")

    def test_func(self):
        return self.request.user.is_staff

    def form_valid(self, form):
        obj = self.get_object()
        messages.success(
            self.request,
            (
                f'Character "{obj.name}" '
                "deleted successfully."
            ),
        )
        return super().form_valid(form)
