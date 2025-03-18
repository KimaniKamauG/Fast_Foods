# REPRESENTS ITEMS ON THE MENU

from django.db import models

# Create your models here.
class MenuItem(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=5, decimal_places=2)
    category = models.CharField(max_length=50)
    available = models.BooleanField(default=True)

    def __str__(self):
        return self.name