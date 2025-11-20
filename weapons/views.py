from django.shortcuts import render, get_object_or_404
from .models import Weapon

# Create your views here.


def weapon_list(request):
    weapons = Weapon.objects.all()
    return render(request, 'weapons/weapon_list.html', {'weapons': weapons})


def weapon_detail(request, pk):
    weapon = get_object_or_404(Weapon, pk=pk)
    return render(request, 'weapons/weapon_detail.html', {'weapon': weapon})
