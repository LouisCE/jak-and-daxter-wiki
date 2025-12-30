from django.urls import path
from . import views

urlpatterns = [
    # Eco Colours CRUD
    path("colours/create/", views.colour_create, name="colour_create"),
    path(
        "colours/<int:pk>/update/",
        views.colour_update,
        name="colour_update",
    ),
    path(
        "colours/<int:pk>/delete/",
        views.colour_delete,
        name="colour_delete",
    ),

    # Weapon Mod CRUD
    path("", views.weapon_list, name="weapon_list"),
    path("create/", views.create_weapon, name="create_weapon"),
    path("weapon/<int:pk>/", views.weapon_detail, name="weapon_detail"),
    path("weapon/<int:pk>/edit/", views.update_weapon, name="update_weapon"),
    path("weapon/<int:pk>/delete/", views.delete_weapon, name="delete_weapon"),
    path("rate-weapons/", views.rate_weapons, name="rate_weapons"),
    path('rankings/', views.weapon_rankings, name='weapon_rankings'),


    # Morph Gun Upgrade CRUD
    path("upgrades/create/", views.create_upgrade, name="create_upgrade"),
    path(
        "upgrades/<int:pk>/edit/",
        views.update_upgrade,
        name="update_upgrade",
    ),
    path(
        "upgrades/<int:pk>/delete/",
        views.delete_upgrade,
        name="delete_upgrade",
    ),
]
