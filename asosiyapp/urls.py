from django.urls import path
from .views import AsosiySahifaView

urlpatterns = [
    path("", AsosiySahifaView, name='home'),
]