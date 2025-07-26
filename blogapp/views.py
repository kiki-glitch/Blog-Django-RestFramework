from django.shortcuts import render
from blogapp.serializers import UserRegistrationSerializer
from rest_framework.response import Response

# Create your views here.
def register_user(request):
    serializer = UserRegistrationSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)