from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from .models import Artist, Canvas, Design, Artwork
from .forms import ArtworkForm

# Create your views here.


def all_artworks(request):
    """ A view to show all artworks, incl. sort & search """

    artworks = Artwork.objects.all()
    query = None
    canvasses = None
    designs = None
    sort = None
    direction = None

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey

            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            artworks = artworks.order_by(sortkey)

        if 'canvas' in request.GET:
            canvasses = request.GET['canvas'].split(',')
            artworks = artworks.filter(canvas__name__in=canvasses)
            canvasses = Canvas.objects.filter(name__in=canvasses)

        if 'design' in request.GET:
            designs = request.GET['design'].split(',')
            artworks = artworks.filter(design__name__in=designs)
            designs = Design.objects.filter(name__in=designs)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "Please enter criteria to search.")
                return redirect(reverse('artworks'))

            queries = (
                Q(friendly_name__icontains=query) |
                Q(artist__full_name__icontains=query) |
                Q(design__description__icontains=query) |
                Q(design__material__icontains=query) |
                Q(canvas__description__icontains=query) |
                Q(canvas__material__icontains=query))
            artworks = artworks.filter(queries)

    current_sorting = f'{sort}_{direction}'

    context = {
        'artworks': artworks,
        'search_term': query,
        'current_canvasses': canvasses,
        'current_designs': designs,
        'current_sorting': current_sorting,
    }

    return render(request, 'artworks/artworks.html', context)


def artwork_detail(request, artwork_id):
    """ A view to show individual artwork details """

    artwork = get_object_or_404(Artwork, pk=artwork_id)

    context = {
        'artwork': artwork,
    }

    return render(request, 'artworks/artwork_detail.html', context)


def all_designs(request):
    """ A view to show all designs """

    designs = Design.objects.all()

    context = {
        'designs': designs,
    }

    return render(request, 'artworks/designs.html', context)


def all_canvasses(request):
    """ A view to show all canvasses """

    canvasses = Canvas.objects.all()

    context = {
        'canvasses': canvasses,
    }

    return render(request, 'artworks/canvasses.html', context)


@login_required
def add_artwork(request):
    """ Add an artwork to the gallery """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only gallery curators can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = ArtworkForm(request.POST, request.FILES)
        if form.is_valid():
            artwork = form.save()
            messages.success(request, 'Successfully added artwork!')
            return redirect(reverse('artwork_detail', args=[artwork.id]))
        else:
            messages.error(
                request,
                'Failed to add artwork. '
                'Please ensure the form is valid.')
    else:
        form = ArtworkForm()
    template = 'artworks/add_artwork.html'
    context = {
        'form': form,
    }

    return render(request, template, context)


@login_required
def edit_artwork(request, artwork_id):
    """ Edit an artwork in the gallery """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only gallery curators can do that.')
        return redirect(reverse('home'))

    artwork = get_object_or_404(Artwork, pk=artwork_id)
    if request.method == 'POST':
        form = ArtworkForm(request.POST, request.FILES, instance=artwork)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated artwork!')
            return redirect(reverse('artwork_detail', args=[artwork.id]))
        else:
            messages.error(
                request,
                'Failed to update artwork. Please ensure the form is valid.')
    else:
        form = ArtworkForm(instance=artwork)
        messages.info(request, f'You are editing {artwork.friendly_name}')

    template = 'artworks/edit_artwork.html'
    context = {
        'form': form,
        'artwork': artwork,
    }

    return render(request, template, context)


@login_required
def delete_artwork(request, artwork_id):
    """ Delete an artwork from the gallery """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only gallery curators can do that.')
        return redirect(reverse('home'))

    artwork = get_object_or_404(Artwork, pk=artwork_id)
    artwork.delete()
    messages.success(request, 'Artwork deleted!')
    return redirect(reverse('artworks'))
