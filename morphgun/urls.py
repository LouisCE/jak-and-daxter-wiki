from django.urls import path
from . import views

urlpatterns = [
    # Eco colours CRUD
    path("colours/create/", views.colour_create, name="colour_create"),
    path("colours/<int:pk>/update/", views.colour_update, name="colour_update"),
    path("colours/<int:pk>/delete/", views.colour_delete, name="colour_delete"),

    # Weapon mod CRUD
    path('', views.weapon_list, name='weapon_list'),
    path('create/', views.create_weapon, name='create_weapon'),
    path('weapon/<int:pk>/', views.weapon_detail, name='weapon_detail'),
    path('weapon/<int:pk>/edit/', views.update_weapon, name='update_weapon'),
    path('weapon/<int:pk>/delete/', views.delete_weapon, name='delete_weapon'),
    path('rate-weapons/', views.rate_weapons, name='rate_weapons'),
]
