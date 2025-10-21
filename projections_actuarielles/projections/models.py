from django.db import models

# Create your models here.
from django.db import models

class Projection(models.Model):
    nom = models.CharField(max_length=100)
    montant = models.DecimalField(max_digits=10, decimal_places=2)
    date_projection = models.DateField()
    description = models.TextField(blank=True)

    def __str__(self):
        return f"{self.nom} - {self.montant} FCFA"
