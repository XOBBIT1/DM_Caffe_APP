from rest_framework import generics

from .models import Basket
from .serializers import BasketSerializer


class BasketAPIView(generics.ListAPIView):
    queryset = Basket.objects.all()
    serializer_class = BasketSerializer
