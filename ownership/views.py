from django.shortcuts import render, get_object_or_404, redirect
from .models import Landowner
from django.http import HttpResponse
from django.contrib import messages
from .forms import LandownerForm, LandPropertyForm

# Create your views here.

def home(request):
    context = {
        'landowners': Landowner.objects.all()
        
    }
    return render(request, 'ownership/home.html', context)

def about(request):
    return render(request, 'ownership/about.html', {'title': 'About'})

def landowner_list(request):
    landowners = Landowner.objects.all()
    return render(request, 'ownership/landowner_list.html', {'landowners': landowners})

def property_list(request, landowner_id):
    landowner = get_object_or_404(Landowner, pk=landowner_id)
    properties = Property.objects.filter(landowner=landowner)
    return render(request, 'ownership/property_list.html', {'landowner': landowner, 'properties': properties})

# def Landowner_Form(request):
#     if request.method == 'POST':
#         form = LandownerForm(request.POST)
#         if form.is_valid():
#             form.save()
#             messages.success(request, f'Land Issues Created Already')
#             return redirect('ownership-home')
#     else:
#         form = LandownerForm()
#     return render(request, 'ownership/ownership_form.html', {'form': form})

def Landowner_Form(request):
    if request.method == 'POST':
        form = LandownerForm(request.POST)
        if form.is_valid():
            landowner = form.save()
            return redirect('ownership-home')
    else:
        form = LandownerForm()
    return render(request, 'ownership/ownership_form.html', {'form': form})

def Landproperty_Form(request):
    if request.method == 'POST':
        form = LandPropertyForm(request.POST)
        if form.is_valid():
            land_property = form.save()
            return redirect('ownership-home')
    else:
        form = LandPropertyForm()
    return render(request, 'ownership/ownership_form.html', {'form': form})

