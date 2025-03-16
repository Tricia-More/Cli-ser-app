from django.shortcuts import render
from django.http import JsonResponse

def hello_world(request):
    return JsonResponse({"message": "Hello!"})
def weather(request):
    return JsonResponse({"message": "The Weather is 30 degrees Celsius"})
def nam(request):
    return JsonResponse({"message": "My Name is Tricia More and this is a Demonstration of my Simple Client-Server Application"})

# Create your views here.
