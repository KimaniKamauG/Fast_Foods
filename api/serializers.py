from rest_framework import serializers
from restaurant.models import MenuItem 
from orders.models import OrderItem, Order
from django.contrib.auth import get_user_model 

User = get_user_model() 


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User 
        fields = ['id', 'email', 'username']

class MenuItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuItem 
        fields = '__all__'

class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem 
        fields = '__all__'

class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True)
    class Meta:
        model = Order
        fields = ['id', 'user', 'items', 'total_price', 'status', 'delivery_address', 'created_at']