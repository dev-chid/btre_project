from django.shortcuts import render
from listings.models import Listing
from listings.choices import price_choices, bedroom_choices, state_choices


def index(request):
    listings = Listing.objects.all()[:1]
    context = {
        'listings': listings,
        'state_choices': state_choices,
        'bedroom_choices': bedroom_choices,
        'price_choices': price_choices,
    }
    return render(request, 'pages/index.html', context)

def about(request):
    return render(request, 'pages/about.html')
