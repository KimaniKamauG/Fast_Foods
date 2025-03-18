from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your models here.
class MenuItem(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    preparation_time = models.PositiveIntegerField(help_text='Minutp es')

class Order(models.Model):
    STATUS_CHOICES = [
        ('Preparing', 'Preparing'),
        ('Out for Delivery', 'Out for Delivery'),
        ('Delivered', 'Delivered'),
        ('Cancelled', 'Cancelled'),
    ]
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    items = models.ManyToManyField('OrderItem')
    total = models.DecimalField(max_digits=8, decimal_places=2)
    #delivery_address = models.PointField(geography=True)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default='Preparing')