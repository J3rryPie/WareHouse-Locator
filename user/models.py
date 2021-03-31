from django.db import models

class City(models.Model):
    x_coordinate = models.DecimalField(max_digits=6,decimal_places=3)
    y_coordinate = models.DecimalField(max_digits=6,decimal_places=3)
    store=models.BooleanField()
    warehouse=models.BooleanField()


