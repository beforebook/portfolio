from django.shortcuts import *
from django.contrib import *
from gallery.models import *

def home(request):
    gallery = Gallery.objects
    return render(request, 'home.html', {'gallery': gallery})