from django.contrib import admin
from .models import Projection  # <-- Import correct depuis ton app locale

admin.site.register(Projection)
