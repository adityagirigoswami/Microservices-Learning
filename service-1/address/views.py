from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Address
from .serializers import AddressSerializer  

class AddressListandCreate(APIView):
    def get(self, request , user_id):
        addresses = Address.objects.filter(user_id=user_id)
        serializer = AddressSerializer(addresses, many=True)
        return Response(serializer.data)

    def post(self, request , user_id):
        data = request.data.copy()
        data['user_id'] = user_id
        serializer = AddressSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

