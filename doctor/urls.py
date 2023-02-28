from django.urls import path
from .views import *

urlpatterns = [
    path('index.html',index),
    path('about.html', about),
    path('contact.html', contact),
    path('services.html', services),
]