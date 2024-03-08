from django.shortcuts import render, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
from django.views.generic import (ListView,
                                  DetailView,
                                  CreateView,
                                  UpdateView,
                                  DeleteView)
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
    paginate_by = 2

class UserLandListView(ListView):
    model = Land
    template_name = 'ownership/user_lands.html' #<app>/<model>_<viewtype>.html
    context_object_name = 'lands'
    ordering = ['-date_created']
    paginate_by = 2

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return Land.objects.filter(operator=user).order_by('-date_created')


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

class LandUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
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
    
    def test_func(self):
        land = self.get_object()
        if self.request.user == land.operator:
            return True
        return False

class LandDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Land
    success_url = '/'

    def test_func(self):
        land = self.get_object()
        if self.request.user == land.operator:
            return True
        return False

def about(request):
    return render(request, 'ownership/about.html', {'title': 'About'})

