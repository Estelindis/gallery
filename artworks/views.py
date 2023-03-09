from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from .models import Artwork

# Create your views here.


def all_artworks(request):
    """ A view to show all artworks, incl. sort & search """

    artworks = Artwork.objects.all()
    query = None

    if request.GET:
        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "Please enter criteria to search.")
                return redirect(reverse('artworks'))

            queries = (
                Q(friendly_name__icontains=query) |
                Q(sku__icontains=query))
            artworks = artworks.filter(queries)

    context = {
        'artworks': artworks,
        'search_term': query,
    }

    return render(request, 'artworks/artworks.html', context)


def artwork_detail(request, artwork_id):
    """ A view to show individual artwork details """

    artwork = get_object_or_404(Artwork, pk=artwork_id)

    context = {
        'artwork': artwork,
    }

    return render(request, 'artworks/artwork_detail.html', context)
