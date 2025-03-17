from django.shortcuts import render
from django.http import JsonResponse

def hello_world(request):
    return JsonResponse({"Server": "Hello!"})
def weather(request):
    return JsonResponse({"Server": "The Weather is 30 degrees Celsius"})
def nam(request):
    return JsonResponse({"Server": "My Name is Tricia More and this is a Demonstration of my Simple Client-Server Application"})
def ask(request):
    return JsonResponse({"Server": "How are you?"})
def resp(request):
    return JsonResponse({"Server": "Good to know!"})

# Create your views here.
