from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import user_passes_test

from .models import Weapon
from .forms import WeaponForm


# List view
def weapon_list(request):
    weapons = Weapon.objects.all()
    return render(request, 'weapons/weapon_list.html', {'weapons': weapons})


# Detail view
def weapon_detail(request, pk):
    weapon = get_object_or_404(Weapon, pk=pk)
    return render(request, 'weapons/weapon_detail.html', {'weapon': weapon})


# Staff-only check
def staff_check(user):
    return user.is_staff


# Create view
@user_passes_test(staff_check)
def create_weapon(request):
    if request.method == 'POST':
        form = WeaponForm(request.POST)
        if form.is_valid():
            weapon = form.save()
            return redirect('weapon_detail', pk=weapon.pk)
    else:
        form = WeaponForm()
    return render(request, 'weapons/create_weapon.html', {'form': form})
