# from django.shortcuts import render
# from .serializers import ProSerializers
# from rest_framework import viewsets
# from .models import Pro
# import requests


# # Create your views here.
# def users(request):
#     #pull data from third party rest api
#     response = requests.get('https://jsonplaceholder.typicode.com/users')
    

# class ProView(viewsets.ModelViewSet):  
#     serializer_class = ProSerializers  
#     queryset = Pro.objects.all()
from django.shortcuts import render
from django.http import HttpResponse
import requests
# Create your views here.
def users(request):
    #pull data from third party rest api
    response = requests.get('https://jsonplaceholder.typicode.com/users')
    #convert reponse data into json
    users = response.json()
    print(users)
    return HttpResponse("Users")
    pass

