from django.contrib.gis.db import models


class Provider(models.Model):
    """
    """
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    language = models.CharField(max_length=50)
    currency = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=15, blank=True)

    def __str__(self):
        return self.name


class ServiceArea(models.Model):
    """
    """
    provider = models.ForeignKey(Provider, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    price = models.FloatField(blank=True, default=None)
    area = models.IntegerField()
    mpoly = models.MultiPolygonField()

    def __str__(self):
        return self.name
