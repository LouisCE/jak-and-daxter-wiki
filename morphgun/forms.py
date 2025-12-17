from django import forms
from .models import Weapon, Colour
from .models import WeaponRating


class ColourForm(forms.ModelForm):
    class Meta:
        model = Colour
        fields = ["name", "description", "image"]


class WeaponForm(forms.ModelForm):
    class Meta:
        model = Weapon
        fields = ['name', 'colour', 'description', 'image']

class WeaponRatingForm(forms.ModelForm):
    class Meta:
        model = WeaponRating
        fields = ['score']
        widgets = {
            'score': forms.Select(
                choices=[(i, i) for i in range(1, 11)],
                attrs={'class': 'form-select'}
            )
        }
