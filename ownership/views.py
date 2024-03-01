from django.shortcuts import render
from django.views.generic import (ListView,
                                  DetailView,
                                  CreateView)
from .models import Land

# Create your views here.

def home(request):
    context = {
        'lands': Land.objects.all()
    }
    return render(request, 'ownership/home.html', context)

class LandListView(ListView):
    model = Land
    template_name = 'ownership/home.html' #<app>/<model>_<viewtype>.html
    context_object_name = 'lands'
    ordering = ['-date_created']

class LandDetailView(DetailView):
    model = Land

class LandCreateView(CreateView):
    model = Land
    field = ['land_location', 'X1_point', 'Y1_point',
             'X2_point', 'Y2_point',
             'X3_point', 'Y3_point',
             'X4_point', 'Y4_point',
             'land_type', 'landmark',
             'LGA', 'state', 'size_of_land',]

def about(request):
    return render(request, 'ownership/about.html', {'title': 'About'})
