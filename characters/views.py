from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Character

class CharacterList(ListView):
    model = Character
    template_name = "characters/character_list.html"
    context_object_name = "characters"

class CharacterDetail(DetailView):
    model = Character
    template_name = "characters/character_detail.html"

class CharacterCreate(CreateView):
    model = Character
    fields = "__all__"
    template_name = "characters/character_form.html"
    success_url = reverse_lazy("character_list")

class CharacterUpdate(UpdateView):
    model = Character
    fields = "__all__"
    template_name = "characters/character_form.html"
    success_url = reverse_lazy("character_list")

class CharacterDelete(DeleteView):
    model = Character
    template_name = "characters/character_confirm_delete.html"
    success_url = reverse_lazy("character_list")
