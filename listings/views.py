from django.shortcuts import get_object_or_404, render
from django.core.paginator import Paginator, Page
from .models import Listing

def index(request):
    listings = Listing.objects.all()
    paginator = Paginator(listings, 2)

    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)

    context = {
        'listings': page_obj
    }
    return render(request, 'listings/listings.html', context)

def listing(request, listing_id):
    listing = get_object_or_404(Listing, pk=listing_id)
    context = {
        'listing': listing
    }
    return render(request, 'listings/listing.html', context)

def search(request):
    return render(request, 'listings/search.html')