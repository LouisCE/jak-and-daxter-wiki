from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.exceptions import PermissionDenied
from .models import Colour, Weapon, WeaponRating, MorphGunUpgrade
from django.db.models import Avg, Count, OuterRef, Subquery
from .forms import WeaponForm, ColourForm, MorphGunUpgradeForm


# Weapon CRUD

# List view
def weapon_list(request):
    weapons = Weapon.objects.select_related('colour')
    colours = Colour.objects.all()

    return render(
        request,
        'morphgun/weapon_list.html',
        {
            'weapons': weapons,
            'colours': colours,
        }
    )


# Detail view
def weapon_detail(request, pk):
    weapon = get_object_or_404(Weapon, pk=pk)

    jak2_upgrades = weapon.upgrades.filter(game="jak2")
    jak3_upgrades = weapon.upgrades.filter(game="jak3")

    return render(
        request,
        'morphgun/weapon_detail.html',
        {
            'weapon': weapon,
            'jak2_upgrades': jak2_upgrades,
            'jak3_upgrades': jak3_upgrades,
        },
    )


# Create view
def create_weapon(request):
    if not request.user.is_staff:
        raise PermissionDenied
    if request.method == 'POST':
        form = WeaponForm(request.POST)
        if form.is_valid():
            weapon = form.save()
            messages.success(
                request,
                f"Weapon '{weapon.name}' created successfully!",
            )
            return redirect('weapon_detail', pk=weapon.pk)
    else:
        form = WeaponForm()

    return render(
        request,
        'morphgun/create_weapon.html',
        {'form': form},
    )


# Update view
def update_weapon(request, pk):
    if not request.user.is_staff:
        raise PermissionDenied
    weapon = get_object_or_404(Weapon, pk=pk)

    if request.method == 'POST':
        form = WeaponForm(
            request.POST,
            request.FILES,
            instance=weapon,
        )
        if form.is_valid():
            weapon = form.save()
            messages.success(
                request,
                f"Weapon '{weapon.name}' updated successfully!",
            )
            return redirect('weapon_detail', pk=weapon.pk)
    else:
        form = WeaponForm(instance=weapon)

    return render(
        request,
        'morphgun/update_weapon.html',
        {
            'form': form,
            'weapon': weapon,
        },
    )


# Delete view
def delete_weapon(request, pk):
    if not request.user.is_staff:
        raise PermissionDenied
    weapon = get_object_or_404(Weapon, pk=pk)

    if request.method == 'POST':
        name = weapon.name
        weapon.delete()
        messages.success(
            request,
            f"Weapon '{name}' deleted successfully!",
        )
        return redirect('weapon_list')

    return render(
        request,
        'morphgun/delete_weapon.html',
        {'weapon': weapon},
    )


# Morph Gun Upgrade CRUD
@login_required
def create_upgrade(request):
    if not request.user.is_staff:
        raise PermissionDenied

    if request.method == 'POST':
        form = MorphGunUpgradeForm(request.POST)
        if form.is_valid():
            upgrade = form.save()
            messages.success(
                request,
                f"Upgrade '{upgrade.name}' created successfully!",
            )

            weapon = upgrade.weapons.first()
            if weapon:
                return redirect('weapon_detail', pk=weapon.pk)

            return redirect('weapon_list')
    else:
        form = MorphGunUpgradeForm()

    return render(
        request,
        'morphgun/upgrade_form.html',
        {
            'form': form,
            'title': 'Create Upgrade',
            'button_text': 'Create Upgrade',
        },
    )


@login_required
def update_upgrade(request, pk):
    if not request.user.is_staff:
        raise PermissionDenied

    upgrade = get_object_or_404(MorphGunUpgrade, pk=pk)

    if request.method == 'POST':
        form = MorphGunUpgradeForm(
            request.POST,
            instance=upgrade,
        )
        if form.is_valid():
            upgrade = form.save()
            messages.success(
                request,
                f"Upgrade '{upgrade.name}' updated successfully!",
            )

            weapon = upgrade.weapons.first()
            if weapon:
                return redirect('weapon_detail', pk=weapon.pk)

            return redirect('weapon_list')
    else:
        form = MorphGunUpgradeForm(instance=upgrade)

    return render(
        request,
        'morphgun/upgrade_form.html',
        {
            'form': form,
            'title': 'Edit Upgrade',
            'button_text': 'Save Changes',
        },
    )


@login_required
def delete_upgrade(request, pk):
    if not request.user.is_staff:
        raise PermissionDenied

    upgrade = get_object_or_404(MorphGunUpgrade, pk=pk)

    if request.method == 'POST':
        weapon = upgrade.weapons.first()
        name = upgrade.name
        upgrade.delete()

        messages.success(
            request,
            f"Upgrade '{name}' deleted successfully!",
        )

        if weapon:
            return redirect('weapon_detail', pk=weapon.pk)

        return redirect('weapon_list')

    return render(
        request,
        'morphgun/upgrade_confirm_delete.html',
        {'upgrade': upgrade},
    )


# Colour CRUD
def colour_create(request):
    if not request.user.is_staff:
        raise PermissionDenied
    if request.method == 'POST':
        form = ColourForm(request.POST, request.FILES)
        if form.is_valid():
            colour = form.save()
            messages.success(
                request,
                f"Colour '{colour.name}' created successfully!",
            )
            return redirect('weapon_list')
    else:
        form = ColourForm()

    return render(
        request,
        'morphgun/create_colour.html',
        {'form': form},
    )


def colour_update(request, pk):
    if not request.user.is_staff:
        raise PermissionDenied
    colour = get_object_or_404(Colour, pk=pk)

    if request.method == 'POST':
        form = ColourForm(
            request.POST,
            request.FILES,
            instance=colour,
        )
        if form.is_valid():
            form.save()
            messages.success(
                request,
                f"Colour '{colour.name}' updated successfully!",
            )
            return redirect('weapon_list')
    else:
        form = ColourForm(instance=colour)

    return render(
        request,
        'morphgun/update_colour.html',
        {
            'form': form,
            'colour': colour,
        },
    )


def colour_delete(request, pk):
    if not request.user.is_staff:
        raise PermissionDenied
    colour = get_object_or_404(Colour, pk=pk)

    if request.method == 'POST':
        name = colour.name
        colour.delete()
        messages.success(
            request,
            f"Colour '{name}' deleted.",
        )
        return redirect('weapon_list')

    return render(
        request,
        'morphgun/delete_colour.html',
        {'colour': colour},
    )


@login_required
def rate_weapons(request):
    user = request.user

    # Get user's existing rating per weapon
    user_rating_subquery = WeaponRating.objects.filter(
        user=user,
        weapon=OuterRef('pk'),
    ).values('score')[:1]

    weapons = (
        Weapon.objects
        .annotate(
            user_score=Subquery(user_rating_subquery),
        )
        .order_by('order')
    )

    if request.method == 'POST':
        for weapon in weapons:
            score = request.POST.get(f"weapon_{weapon.id}")

            if not score:
                messages.error(
                    request,
                    "You must rate all weapons before submitting.",
                )
                return redirect('rate_weapons')

            WeaponRating.objects.update_or_create(
                user=user,
                weapon=weapon,
                defaults={'score': score},
            )

        messages.success(
            request,
            "Your weapon ratings have been saved.",
        )

    # User rankings
    user_ratings = (
        WeaponRating.objects
        .filter(user=user)
        .select_related('weapon')
        .order_by('-score')
    )

    # Community rankings
    community_rankings = (
        Weapon.objects
        .annotate(
            avg_rating=Avg('ratings__score'),
            rating_count=Count('ratings'),
        )
        .filter(rating_count__gt=0)
        .order_by('-avg_rating', '-rating_count')
    )

    return render(
        request,
        'morphgun/rate_weapons.html',
        {
            'weapons': weapons,
            'range': range(1, 11),
            'user_ratings': user_ratings,
            'community_rankings': community_rankings,
        },
    )
