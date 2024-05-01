from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    context = {'title': 'Материалы для преподавания и самоподготовки'}
    return render(request, 'main/index.html', context)

def authorization(request):
    context = {'title': 'Авторизация'}
    return render(request, 'main/authorization.html', context)

def registration(request):
    context = {'title': 'Регистрация'}
    return render(request, 'main/registration.html', context)

def reminder(request):
    context = {'title': 'Напомнить пароль'}
    return render(request, 'main/reminder.html', context)

