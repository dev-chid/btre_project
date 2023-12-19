from django.shortcuts import render
from listings.models import Listing


def index(request):
    listings = Listing.objects.all()[:1]
    context = {
        'listings': listings
    }
    return render(request, 'pages/index.html', context)

def about(request):
    return render(request, 'pages/about.html')
