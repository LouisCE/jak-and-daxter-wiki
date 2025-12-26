from django.urls import path
from .views import (
    CharacterList, CharacterDetail,
    CharacterCreate, CharacterUpdate, CharacterDelete
)

urlpatterns = [
    path('', CharacterList.as_view(), name='character_list'),
    path('create/', CharacterCreate.as_view(), name='character_create'),
    path('<int:pk>/', CharacterDetail.as_view(), name='character_detail'),
    path('<int:pk>/edit/', CharacterUpdate.as_view(), name='character_update'),
    path(
        '<int:pk>/delete/',
        CharacterDelete.as_view(),
        name='character_delete'
    ),
]
