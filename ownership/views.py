from django.shortcuts import render

lands = [
    {
        'name': 'Renny',
        'location': 'ekehuan road',
        'size_of_land': '100ft by 100ft'
    },
    {
        'name': 'Mike',
        'location': 'Sapele road',
        'size_of_land': '1200ft by 100ft'
    }

]

# Create your views here.

def home(request):
    context = {
        'lands': lands
    }
    return render(request, 'ownership/home.html', context)

def about(request):
    return render(request, 'ownership/about.html')