from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from django.contrib.auth import get_user_model
from rest_framework import permissions
from rest_framework.views import APIView

from .models import Address, Client
from .serializers import ClientSerializer


class ClientViewSet(viewsets.ModelViewSet):
    queryset = get_user_model().objects.all()
    serializer_class = ClientSerializer
    permission_classes = (permissions.IsAuthenticated,)

    @action(methods=['get'], detail=False)
    def addresses(self, request):
        addresses = Address.objects.all().values()
        return Response({'addresses': [address for address in addresses]})


class AddProductToBasketAPIView(APIView):
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request, **kwargs):
        try:
            pk = kwargs.get("pk", None)
            client = Client.objects.get(pk=pk)
        except Exception:
            return Response({"error": " Such client dosen't exist!"}, status=404)
        return Response({"products": client.products_basket.all().values()})

    def post(self, request, **kwargs):
        try:
            pk = kwargs.get("pk", None)
            client = Client.objects.get(pk=pk)
        except Exception:
            return Response({"error": " Such client dosen't exist!"}, status=404)

        product_id = request.data.get("product_id")
        if not product_id:
            return Response({"error": "product_id is required"}, status=status.HTTP_400_BAD_REQUEST)

        client.products_basket.add(product_id)
        return Response('Product added to basket')

    def delete(self, request, **kwargs):
        try:
            pk = kwargs.get("pk", None)
            client = Client.objects.get(pk=pk)
        except Exception:
            return Response({"error": " Such client dosen't exist!"}, status=404)

        product_id = request.data.get("product_id")
        if not product_id:
            return Response({"error": "product_id is required"}, status=status.HTTP_400_BAD_REQUEST)

        client.products_basket.remove(product_id)
        return Response('Product deleted from basket')
