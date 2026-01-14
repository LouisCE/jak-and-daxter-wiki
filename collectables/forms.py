from django import forms
from .models import Collectable


class CollectableForm(forms.ModelForm):
    class Meta:
        model = Collectable
        fields = ['name', 'description', 'image', 'order']
