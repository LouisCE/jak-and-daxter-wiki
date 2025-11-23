from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import user_passes_test

from .models import Weapon
from .forms import WeaponForm


# List view
def weapon_list(request):
    weapons = Weapon.objects.all()
    return render(request, 'morphgun/weapon_list.html', {'weapons': weapons})


# Detail view
def weapon_detail(request, pk):
    weapon = get_object_or_404(Weapon, pk=pk)
    return render(request, 'morphgun/weapon_detail.html', {'weapon': weapon})


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
    return render(request, 'morphgun/create_weapon.html', {'form': form})


# Update view
@user_passes_test(staff_check)
def update_weapon(request, pk):
    weapon = get_object_or_404(Weapon, pk=pk)
    if request.method == 'POST':
        form = WeaponForm(request.POST, request.FILES, instance=weapon)
        if form.is_valid():
            form.save()
            return redirect('weapon_detail', pk=weapon.pk)
    else:
        form = WeaponForm(instance=weapon)
    return render(request, 'morphgun/update_weapon.html', {'form': form, 'weapon': weapon})


# Delete view
@user_passes_test(staff_check)
def delete_weapon(request, pk):
    weapon = get_object_or_404(Weapon, pk=pk)
    if request.method == 'POST':
        weapon.delete()
        return redirect('weapon_list')
    return render(request, 'morphgun/delete_weapon.html', {'weapon': weapon})
