# THIS SETUP PROVIDES ENDPOINTS LIKE 'api/menu/' FOR MENU ITEMS AND
# 'api/orders/' FOR ORDER MANAGEMENT, SECURED WITH AUTHENTICATION...

from django.urls import path, include 
from rest_framework .routers import DefaultRouter 
from .views import MenuItemViewSet, OrderViewSet, UserViewSet
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView 

router = DefaultRouter()
router.register(r'menu', MenuItemViewSet)
router.register(r'orders', OrderViewSet)
router.register('users', UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
] 

urlpatterns += router.urls