from django.urls import path, include
from .views import ClientViewSet, AddProductToBasketAPIView
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'', ClientViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('basket/<int:pk>/', AddProductToBasketAPIView.as_view()),
]
