from django.shortcuts import render
from .models import Land

# Create your views here.

def home(request):
    context = {
        'lands': Land.objects.all()
    }
    return render(request, 'ownership/home.html', context)

def about(request):
    return render(request, 'ownership/about.html', {'title': 'About'})
