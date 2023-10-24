from django.db import models

class PurchaseLocation(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=255)
    purchase_location = models.ForeignKey(PurchaseLocation, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
