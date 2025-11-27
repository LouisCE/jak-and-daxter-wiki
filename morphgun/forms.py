from django import forms
from .models import Weapon, Colour


class ColourForm(forms.ModelForm):
    class Meta:
        model = Colour
        fields = ["name", "description", "image"]


class WeaponForm(forms.ModelForm):
    class Meta:
        model = Weapon
        fields = ['name', 'colour', 'description', 'image']
