from django.urls import path
from .views import DiaristasCidadeList

urlpatterns = [
    path('diaristas-cidade', DiaristasCidadeList.as_view(), name='diaristas-cidade-list'),
]