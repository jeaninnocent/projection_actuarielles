from django.shortcuts import render

# Create your views here.

# projections_actuarielles/projections/views.py

from django.shortcuts import render
from .models import Projection

def liste_projections(request):
    projections = Projection.objects.all()
    return render(request, 'projections/liste.html', {'projections': projections})
