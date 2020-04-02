from django.shortcuts import *
from django.contrib import *

def home(request):
    return render(request, 'home.html')