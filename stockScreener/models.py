from django.db import models
# Create your models here.

class stock(models.Model):
    stockCode = models.CharField(max_length=10, primary_key=True)
    now = models.IntegerField()
    diff = models.IntegerField(null=True, blank=True)
    rate = models.FloatField(null=True, blank=True)
    high = models.IntegerField(null=True, blank=True)
    low = models.IntegerField(null=True, blank=True)
    quant = models.IntegerField(null=True, blank=True)
    marketSum = models.IntegerField(null=True, blank=True)
