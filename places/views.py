from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Place
from .forms import PlaceForm
import random


def home(request):

    selected_place = None

    if request.method == 'POST':

        places = list(Place.objects.all())

        if places:

            weights = [place.rating for place in places]

            selected_place = random.choices(places, weights=weights, k=1)[0]

    context = {
        'selected_place': selected_place,
    }
    return render(request, 'places/home.html', context)


def places_list(request):

    places = Place.objects.all()
    context = {
        'places': places,
    }
    return render(request, 'places/places_list.html', context)


def place_detail(request, pk):

    place = get_object_or_404(Place, pk=pk)
    context = {
        'place': place,
    }
    return render(request, 'places/place_detail.html', context)


def add_place(request):

    if request.method == 'POST':
        form = PlaceForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Місце успішно додано!')
            return redirect('places_list')
    else:
        form = PlaceForm()

    context = {
        'form': form,
    }
    return render(request, 'places/add_place.html', context)
