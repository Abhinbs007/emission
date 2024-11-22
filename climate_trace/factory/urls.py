from django.urls import path
from .views import get_emissions_sources

urlpatterns = [
    path('', get_emissions_sources, name='get_emissions_sources'),
]