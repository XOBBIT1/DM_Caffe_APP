from rest_framework import serializers

from .models import Client, Address


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = ['id', 'street_name', 'city_name']


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ['id', 'full_name', 'created_at', 'nickname', 'phone_number', 'email', 'address']
