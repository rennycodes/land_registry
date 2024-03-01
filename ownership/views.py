from django.shortcuts import render
from django.views.generic import ListView, DetailView
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
    

def about(request):
    return render(request, 'ownership/about.html', {'title': 'About'})
