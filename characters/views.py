from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from .models import Character
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


class CharacterList(ListView):
    model = Character
    template_name = "characters/character_list.html"
    context_object_name = "characters"


class CharacterDetail(DetailView):
    model = Character
    template_name = "characters/character_detail.html"


class CharacterCreate(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Character
    fields = "__all__"
    template_name = "characters/character_form.html"
    success_url = reverse_lazy("character_list")

    def test_func(self):
        return self.request.user.is_staff


class CharacterUpdate(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Character
    fields = "__all__"
    template_name = "characters/character_form.html"
    success_url = reverse_lazy("character_list")

    def test_func(self):
        return self.request.user.is_staff


class CharacterDelete(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Character
    template_name = "characters/character_confirm_delete.html"
    success_url = reverse_lazy("character_list")

    def test_func(self):
        return self.request.user.is_staff
