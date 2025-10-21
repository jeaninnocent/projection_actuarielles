from django.urls import path
from .views import liste_projections

urlpatterns = [
    path('', liste_projections, name='liste_projections'),
]
