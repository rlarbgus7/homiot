from django.db import models

# Create your models here.
class Deshboard(models.Model):
    seq = models.IntegerField(primary_key=True)
    temp = models.FloatField(blank=True, null=True)
    hum = models.FloatField(blank=True, null=True)
    gas = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'deshboard'