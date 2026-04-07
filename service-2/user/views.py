from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import UserSerializer
from .models import User
from .services import AddressServiceClient
import uuid

class UserListandCreate(APIView):
    def get(self , request):
        users = User.objects.all()
        serializer = UserSerializer(users , many=True)
        return Response(serializer.data)


    def post(self , request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

class UserRetrieve(APIView):
    def get(self ,request, pk):
        user = User.objects.get(pk=pk)
        user_data = UserSerializer(user).data

        user_data['address'] = AddressServiceClient.get_user_addresses(pk)
        print(user_data['address'])
        return Response(user_data)

    
