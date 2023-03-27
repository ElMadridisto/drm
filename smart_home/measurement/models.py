from django.db import models

# TODO: опишите модели датчика (Sensor) и измерения (Measurement)
class Senser(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=100)

class Measerement(models.Model):
    temperature = models.FloatField()
    date_and_time = models.DateTimeField(auto_now_add=True)
    senser = models.ForeignKey(Senser, on_delete=models.CASCADE)
