from django.contrib import admin
from .models import Colour, Weapon, MorphGunUpgrade


@admin.register(Colour)
class ColourAdmin(admin.ModelAdmin):
    list_display = ("name", "order")
    list_editable = ("order",)
    ordering = ("order",)


@admin.register(Weapon)
class WeaponAdmin(admin.ModelAdmin):
    list_display = ("name", "colour", "order")
    list_editable = ("order",)
    ordering = ("order",)
    list_filter = ("colour",)
    search_fields = ("name",)


@admin.register(MorphGunUpgrade)
class MorphGunUpgradeAdmin(admin.ModelAdmin):
    list_display = ("name", "game")
    list_filter = ("game",)
    search_fields = ("name",)
