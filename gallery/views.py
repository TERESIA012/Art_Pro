from django.shortcuts import render
from django.http  import HttpResponse

# Create your views here.


def index(request):
    images = Image.objects.all()
    locations = Location.get_locations()
    print(locations)
    return render(request, 'photo/index.html', {'images': images[::-1], 'locations': locations})
