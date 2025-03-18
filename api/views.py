from rest_framework import viewsets 
from rest_framework.permissions import IsAuthenticated 
from restaurant.models import MenuItem
from orders.models import Order 
from .serializers import MenuItemSerializer, OrderSerializer 

class MenuItemViewSet(viewsets.ModelViewSet):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer 
    
class OrderViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)



































# from django.shortcuts import render
# from rest_framework import APIView 
# from rest_framework.response import Response 
# from django.contrib.gis.db.models.functions import Distance 

# # Create your views here.
# class RestaurantAPI(APIView):
#     def post(self, request):
#         lat = request.data.get('lat')
#         lng = request.data.get('lng')
#         point = Point(float(lng), float(lat), srid=4326)

#         restaurants = MuhindiFastFoods.objects.annotate(
#             distance=Distance('location', point)
#         ).filter(
#             location__distance_lte=(point, models.F('delivery_radius'))
#         ).order_by('ditance')

#         return Response({
#             'restaurants': [
#                 {
#                     'name':r.name,
#                     'address': r.address,
#                     'distance': r.distance.m
#                 }
#                 for r in restaurants
#             ]
#         })