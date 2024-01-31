from django.shortcuts import render, get_object_or_404
from .models import Landowner, Property
from django.http import HttpResponse

# Create your views here.

def home(request):
    return HttpResponse('<h1>Blog Home</h1>')


def landowner_list(request):
    landowners = Landowner.objects.all()
    return render(request, 'ownership/landowner_list.html', {'landowners': landowners})

def property_list(request, landowner_id):
    landowner = get_object_or_404(Landowner, pk=landowner_id)
    properties = Property.objects.filter(landowner=landowner)
    return render(request, 'ownership/property_list.html', {'landowner': landowner, 'properties': properties})

