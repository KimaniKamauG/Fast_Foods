# REPRESENTS A CUSTOMER'S ORDER

from django.db import models
from restaurant.models import MenuItem 
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your models here.
class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    items = models.ManyToManyField(MenuItem, through='OrderItem')
    total_price = models.DecimalField(max_digits=6, decimal_places=2)
    status = models.CharField(max_length=20, default='Pending')
    delivery_address = models.TextField()
    created_at = models.DateTimeField(auto_now=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Order {self.id} by {self.user}'
    
# LINKS ORDERS TO MENU ITEMS WITH QUANTITIES 

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    menu_item = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()






# IGNORE FOR NOW THE CODE BELOW 

# class MenuItem(models.Model):
#     name = models.CharField(max_length=255)
#     price = models.DecimalField(max_digits=6, decimal_places=2)
#     preparation_time = models.PositiveIntegerField(help_text='Minutes')

# class Order(models.Model):
#     STATUS_CHOICES = [
#         ('Preparing', 'Preparing'),
#         ('Out for Delivery', 'Out for Delivery'),
#         ('Delivered', 'Delivered'),
#         ('Cancelled', 'Cancelled'),
#     ]
#     customer = models.ForeignKey(User, on_delete=models.CASCADE)
#     items = models.ManyToManyField('OrderItem')
#     total = models.DecimalField(max_digits=8, decimal_places=2)
#     #delivery_address = models.PointField(geography=True)
#     status = models.CharField(max_length=1, choices=STATUS_CHOICES, default='Preparing')