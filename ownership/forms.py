from django import forms
from .models import Landowner

class LandownerForm(forms.ModelForm):
    class Meta:
        model = (Landowner)
        fields = ['name', 'contact_number', 'address']
