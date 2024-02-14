from django.shortcuts import render

lands = [
    {
        'Name': 'Renny',
        'location': 'ekehuan road',
        'size of land': '100ft by 100ft'
    },
    {
        'Name': 'Mike',
        'location': 'Sapele road',
        'size of land': '1200ft by 100ft'
    }

]

# Create your views here.

def home(request):
    return render(request, 'ownership/home.html')

def about(request):
    return render(request, 'ownership/about.html')