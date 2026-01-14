from django import forms
from .models import Weapon, Colour, WeaponRating, MorphGunUpgrade


class ColourForm(forms.ModelForm):
    class Meta:
        model = Colour
        fields = ["name", "hex_code", "description", "image", "order"]
        widgets = {
            "hex_code": forms.TextInput(
                attrs={
                    "type": "color",
                    "class": "form-control"
                }
            ),
        }
        labels = {
            "order": "Display order",
        }
        help_texts = {
            "order": "Lower numbers appear first (e.g. 0 = top)",
        }


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


class MorphGunUpgradeForm(forms.ModelForm):
    class Meta:
        model = MorphGunUpgrade
        fields = [
            'name',
            'game',
            'effect',
            'requirement',
            'price',
            'weapons',
        ]
        widgets = {
            'weapons': forms.CheckboxSelectMultiple(),
        }
