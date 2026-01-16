from django.contrib import admin
from .models import Collectable


@admin.register(Collectable)
class CollectableAdmin(admin.ModelAdmin):
    list_display = ("name", "order")
    list_editable = ("order",)
    ordering = ("order",)
