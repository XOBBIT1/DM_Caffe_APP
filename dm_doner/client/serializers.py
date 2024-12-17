from rest_framework import serializers

from .models import Client, Address


class AddressSerializer(serializers.Serializer):
    street_name = serializers.CharField(max_length=255)
    city_name = serializers.CharField(max_length=255)

    def update(self, instance, validated_data):
        instance.street_name = validated_data.get("street_name", instance.street_name)
        instance.city_name = validated_data.get("city_name", instance.city_name)


class ClientSerializer(serializers.Serializer):
    full_name = serializers.CharField(max_length=255)
    created_at = serializers.DateTimeField(read_only=True)
    nickname = serializers.CharField(max_length=255)
    phone_number = serializers.CharField(max_length=255)
    email = serializers.EmailField()
    image = serializers.ImageField(read_only=True)
    address = AddressSerializer()

    def create(self, validated_data):
        address = Address.objects.create(
            street_name=validated_data["address"].get('street_name'),
            city_name=validated_data["address"].get('city_name'),
        )
        validated_data["address"] = address
        return Client.objects.create(**validated_data)

    def update(self, instance, validated_data):
        address = Address.objects.create(
            street_name=validated_data["address"].get('street_name'),
            city_name=validated_data["address"].get('city_name'),
        )
        validated_data["address"] = address
        instance.full_name = validated_data.get("full_name", instance.full_name)
        instance.nickname = validated_data.get("nickname", instance.nickname)
        instance.phone_number = validated_data.get("phone_number", instance.phone_number)
        instance.email = validated_data.get("email", instance.email)
        instance.address = validated_data.get("address")
        instance.save()
        return instance
