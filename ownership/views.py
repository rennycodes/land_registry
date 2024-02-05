from django.shortcuts import render, get_object_or_404, redirect
from .models import Landowner
from django.http import HttpResponse
from django.contrib import messages
from .forms import LandownerForm

# Create your views here.

def home(request):
    context = {
        'landowners': Landowner.objects.all()
        
    }
    return render(request, 'ownership/home.html', context)

def landowner_list(request):
    landowners = Landowner.objects.all()
    return render(request, 'ownership/landowner_list.html', {'landowners': landowners})

def property_list(request, landowner_id):
    landowner = get_object_or_404(Landowner, pk=landowner_id)
    properties = Property.objects.filter(landowner=landowner)
    return render(request, 'ownership/property_list.html', {'landowner': landowner, 'properties': properties})

def Landowner_Form(request):
    if request.method == 'POST':
        form = LandownerForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'Land Issues Created Already')
            return redirect('ownership-form')
    else:
        form = LandownerForm()
    return render(request, 'ownership/ownership_form.html', {'form': form})
