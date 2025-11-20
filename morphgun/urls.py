from django.urls import path
from . import views

urlpatterns = [
    path('', views.weapon_list, name='weapon_list'),
    path('create/', views.create_weapon, name='create_weapon'),
    path('<int:pk>/', views.weapon_detail, name='weapon_detail'),
]
