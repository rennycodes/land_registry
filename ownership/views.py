from django.shortcuts import render, get_object_or_404
from .models import Landowner, Property

# Create your views here.

def landowner_list(request):
    landowners = Landowner.objects.all()
    return render(request, 'ownership/landowner_list.html', {'landowners': landowners})

def property_list(request, landowner_id):
    landowner = get_object_or_404(Landowner, pk=landowner_id)
    properties = Property.objects.filter(landowner=landowner)
    return render(request, 'ownership/property_list.html', {'landowner': landowner, 'properties': properties})
