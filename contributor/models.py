from django.db import models


class City(models.Model):
    city = models.CharField(max_length=100)
    lat = models.CharField(max_length=100)
    lng = models.CharField(max_length=100)
    state = models.CharField(max_length=100)

    class Meta:
        db_table = 'city'
