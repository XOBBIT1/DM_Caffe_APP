from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAdminUser

from .models import Client, Address
from .serializers import ClientSerializer


class ClientViewSet(viewsets.ModelViewSet):
    queryset = Client.objects.all()
    serializer_class = ClientSerializer
    permission_classes = [IsAdminUser,]

    @action(methods=['get'], detail=False)
    def addresses(self, request):
        addresses = Address.objects.all().values()
        return Response({'addresses': [address for address in addresses]})


# class ClientAPIView(APIView):
#
#     def get(self, request):
#         clients = Client.objects.all()
#         serializer_data = ClientSerializer(clients, many=True).data
#         return Response({'clients': serializer_data})
#
#     def post(self, request):
#         if Client.objects.filter(nickname=request.data.get('nickname')):
#             return Response({"error": "Client with such nickname already exist!"}, status=404)
#         if Client.objects.filter(email=request.data.get('email')):
#             return Response({"error": "Client with such email already exist!"}, status=404)
#
#         serializer_data = ClientSerializer(data=request.data)
#         serializer_data.is_valid(raise_exception=True)
#         serializer_data.save()
#         return Response({'client': serializer_data.data})
#
#     def put(self, request, **kwargs):
#         try:
#             pk = kwargs.get("pk", None)
#             instance = Client.objects.get(pk=pk)
#         except Exception:
#             return Response({"error": " Such client dosen't exist!"}, status=404)
#
#         serializer_data = ClientSerializer(data=request.data, instance=instance)
#         serializer_data.is_valid(raise_exception=True)
#         serializer_data.save()
#         return Response({'client': serializer_data.data})
