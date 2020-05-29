from django.db import models

# Create your models here.

class Vehicle(models.Model):
    licence_plate = models.CharField(max_length=10)
    make = models.CharField(max_length=64)
    model = models.CharField(max_length=64)
    color = models.CharField(max_length=32) # TODO: Consider making this a Foreign key for set values?

    def __str__(self):
        return "{}: {} {}".format(self.model, self.licence_plate, self.color)        

class DamageLocation(models.Model):
    location = models.CharField(max_length=128)

    def __str__(self):
        return self.location

class DamageType(models.Model):
    description = models.CharField(max_length=128)

    def __str__(self):
        return self.description

class Damage(models.Model):
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE, related_name='damage')
    location = models.ForeignKey(DamageLocation, on_delete=models.CASCADE, related_name='damage')
    type = models.ForeignKey(DamageType, on_delete=models.CASCADE, related_name='damage')

    def __str__(self):
        return "{}: {} at {}".format(self.vehicle.licence_plate, self.type.description, self.location.location)