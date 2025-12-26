from django.urls import path
from . import views


urlpatterns = [
    path('', views.collectable_list, name='collectable_list'),
    path('create/', views.collectable_create, name='collectable_create'),
    path('<int:pk>/update/',
         views.collectable_update,
         name='collectable_update'),
    path(
        '<int:pk>/delete/',
        views.collectable_delete,
        name='collectable_delete'),
]
