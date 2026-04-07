from rest_framework import serializers
from .models import Address
class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = ['id', 'user_id', 'city', 'state', 'zip_code']

