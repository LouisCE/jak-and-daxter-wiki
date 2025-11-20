from django.urls import path
from . import views

urlpatterns = [
    path('', views.weapon_list, name='weapon_list'),
    path('<int:pk>/', views.weapon_detail, name='weapon_detail'),
]
