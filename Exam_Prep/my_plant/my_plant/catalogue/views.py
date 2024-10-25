from django.shortcuts import render, redirect, get_object_or_404

from my_plant.catalogue.models import Plant
from my_plant.profiles.models import Profile
from my_plant.catalogue.forms import CreatePlantForm, DeletePlantForm


def show_catalogue(request):
    profile = Profile.objects.first()
    plants = Plant.objects.all()

    context = {
        'profile': profile,
        'plants': plants,
    }

    return render(request, 'catalogue.html', context)


def create_plant(request):
    profile = Profile.objects.first()

    if request.method == 'POST':
        form = CreatePlantForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('catalogue')
    else:
        form = CreatePlantForm()

    context = {
        'form': form,
        'profile': profile,
    }
    return render(request, 'create-plant.html', context)


def plant_details(request, pk):
    profile = Profile.objects.first()
    plant = get_object_or_404(Plant, pk=pk)

    context = {
        'plant': plant,
        'profile': profile,
    }
    return render(request, 'plant-details.html', context)


def edit_plant(request, pk):

    profile = Profile.objects.first()
    plant = get_object_or_404(Plant, pk=pk)

    if request.method == 'POST':
        form = CreatePlantForm(request.POST, instance=plant)
        if form.is_valid():
            form.save()
            return redirect('catalogue')
    else:
        form = CreatePlantForm(instance=plant)

    context = {
        'form': form,
        'profile': profile,
        'plant': plant,
    }
    return render(request, 'edit-plant.html', context)


def delete_plant(request, pk):
    profile = Profile.objects.first()
    plant = get_object_or_404(Plant, pk=pk)

    if request.method == 'POST':
        plant.delete()
        return redirect('catalogue')

    form = DeletePlantForm(instance=plant)
    context = {
        'form': form,
        'plant': plant,
        'profile': profile,
    }
    return render(request, 'delete-plant.html', context)
