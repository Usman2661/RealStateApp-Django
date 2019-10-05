from django.shortcuts import get_object_or_404 ,render
from django.core.paginator import EmptyPage, PageNotAnInteger,Paginator

from .models import Listings

# Create your views here.
def index(request):
    listings=Listings.objects.order_by('-list_date').filter(is_published=True)

    paginator=Paginator(listings,6 )
    page = request.GET.get('page')
    paged_listings =paginator.get_page(page)

    context={
         'listings':paged_listings
    }
    return render (request, 'listings/listings.html',context)

def search(request):
    return render (request, 'listings/search.html')
    
def listing(request,listing_id):

    listing = get_object_or_404(Listings, pk=listing_id)

    context={
        'listing':listing
    }

    return render (request, 'listings/listing.html',context)