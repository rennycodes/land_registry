from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (ListView,
                                  DetailView,
                                  CreateView,
                                  UpdateView)
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

class LandCreateView(LoginRequiredMixin, CreateView):
    model = Land
    fields = ['name', 'residential_address',
              'phone_number', 'email',
              'land_location', 'X1_point', 'Y1_point',
              'X2_point', 'Y2_point',
              'X3_point', 'Y3_point',
              'X4_point', 'Y4_point',
              'land_type', 'landmark',
              'LGA', 'state', 'size_of_land',]
    
    def form_valid(self, form):
        form.instance.operator = self.request.user
        return super().form_valid(form)

class LandUpdateView(LoginRequiredMixin, UpdateView):
    model = Land
    fields = ['name', 'residential_address',
              'phone_number', 'email',
              'land_location', 'X1_point', 'Y1_point',
              'X2_point', 'Y2_point',
              'X3_point', 'Y3_point',
              'X4_point', 'Y4_point',
              'land_type', 'landmark',
              'LGA', 'state', 'size_of_land',]
    
    def form_valid(self, form):
        form.instance.operator = self.request.user
        return super().form_valid(form)

def about(request):
    return render(request, 'ownership/about.html', {'title': 'About'})
