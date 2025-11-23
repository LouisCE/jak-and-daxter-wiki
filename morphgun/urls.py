from django.urls import path
from . import views

urlpatterns = [
    path('', views.weapon_list, name='weapon_list'),
    path('create/', views.create_weapon, name='create_weapon'),
    path('weapon/<int:pk>/', views.weapon_detail, name='weapon_detail'),
    path('weapon/<int:pk>/edit/', views.update_weapon, name='update_weapon'),
    path('weapon/<int:pk>/delete/', views.delete_weapon, name='delete_weapon'),
]
