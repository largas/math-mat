from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'main/index.html')

def authorization(request):
    return render(request, 'main/authorization.html')

def registration(request):
    return render(request, 'main/registration.html')

def reminder(request):
    return render(request, 'main/reminder.html')

