from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@api_view(['GET'])
def home(request):
    return Response({"message": "API is working"}, status=200)

@api_view(['POST'])
def register_user(request):
    # handle registration logic here
    return Response({"message": "User registered"}, status=201)

@api_view(['GET'])
def secure_data(request):
    return Response({"message": "Secure data"}, status=200)
