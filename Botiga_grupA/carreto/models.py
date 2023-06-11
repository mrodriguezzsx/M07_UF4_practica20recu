from django.db import models
from django.db import models
from rest_framework.exceptions import ValidationError
from cataleg.models import Producte


class Carreto(models.Model):
    id = models.AutoField(primary_key=True)
    nom_id = models.ForeignKey(Producte, db_column='nom_id', on_delete=models.CASCADE, default=None)
    nom = models.CharField(max_length=100, blank=True, null=True, editable=False, unique=False)
    cantitat = models.DecimalField(max_digits=6, decimal_places=0)
    price = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True, editable=False)

    def __str__(self):
        return self.nom

    class Meta:
        unique_together = (('nom_id'),)

    def save(self, *args, **kwargs):
        unit_price = self.nom_id.preu
        total_price = unit_price * self.cantitat
        self.price = total_price

        try:
            existing_carret = Carreto.objects.get(nom_id=self.nom_id)
        except Carreto.DoesNotExist:
            existing_carret = None

        if existing_carret:
            raise ValidationError('Ya existe')

        self.nom = self.nom_id.nom
        super().save(*args, **kwargs)
