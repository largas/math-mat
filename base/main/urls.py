from django.urls import path
from main import views

app_name = 'main'

urlpatterns = [
    path('', views.index, name='index'),
    path('authorization/', views.authorization, name='authorization'),
    path('registration/', views.registration, name='registration'),
    path('reminder/', views.reminder, name='reminder'),
]