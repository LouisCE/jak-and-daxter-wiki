from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import user_passes_test
from django.contrib import messages

from .models import Weapon, Colour
from .forms import WeaponForm, ColourForm


# Staff-only check
def staff_check(user):
    return user.is_staff

# Weapon CRUD


# List view
def weapon_list(request):
    weapons = (
        Weapon.objects
        .select_related('colour')
        .order_by('order', 'colour__name', 'pk')
    )
    colours = Colour.objects.all().order_by('name')
    template = 'morphgun/weapon_list.html'
    context = {
        'weapons': weapons,
        'colours': colours,
    }
    return render(request, template, context)


# Detail view
def weapon_detail(request, pk):
    weapon = get_object_or_404(Weapon, pk=pk)
    return render(request, 'morphgun/weapon_detail.html', {'weapon': weapon})


# Create view
@user_passes_test(staff_check)
def create_weapon(request):
    if request.method == 'POST':
        form = WeaponForm(request.POST)
        if form.is_valid():
            weapon = form.save()
            messages.success(request, f"Weapon '{weapon.name}' created successfully!")
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
            weapon = form.save()
            messages.success(request, f"Weapon '{weapon.name}' updated successfully!")
            return redirect('weapon_detail', pk=weapon.pk)
    else:
        form = WeaponForm(instance=weapon)
    return render(request, 'morphgun/update_weapon.html', {'form': form, 'weapon': weapon})


# Delete view
@user_passes_test(staff_check)
def delete_weapon(request, pk):
    weapon = get_object_or_404(Weapon, pk=pk)
    if request.method == 'POST':
        name = weapon.name
        weapon.delete()
        messages.success(request, f"Weapon '{name}' deleted successfully!")
        return redirect('weapon_list')
    return render(request, 'morphgun/delete_weapon.html', {'weapon': weapon})


# COLOUR CRUD
@user_passes_test(staff_check)
def colour_create(request):
    if request.method == "POST":
        form = ColourForm(request.POST, request.FILES)
        if form.is_valid():
            colour = form.save()
            messages.success(request, f"Colour '{colour.name}' created successfully!")
            return redirect("weapon_list")  # Redirect to morphgun page
    else:
        form = ColourForm()
    return render(request, "morphgun/create_colour.html", {"form": form})

@user_passes_test(staff_check)
def colour_update(request, pk):
    colour = get_object_or_404(Colour, pk=pk)
    if request.method == "POST":
        form = ColourForm(request.POST, request.FILES, instance=colour)
        if form.is_valid():
            form.save()
            messages.success(request, f"Colour '{colour.name}' updated successfully!")
            return redirect("weapon_list")
    else:
        form = ColourForm(instance=colour)

    return render(request, "morphgun/update_colour.html", {
        "form": form,
        "colour": colour
    })

@user_passes_test(staff_check)
def colour_delete(request, pk):
    colour = get_object_or_404(Colour, pk=pk)

    if request.method == "POST":
        name = colour.name
        colour.delete()
        messages.success(request, f"Colour '{name}' deleted.")
        return redirect("weapon_list")

    return render(request, "morphgun/delete_colour.html", {"colour": colour})
