from django.shortcuts import render, redirect, get_object_or_404
from worldOfSpeed.cars.froms import CarForm, DeleteCarForm
from worldOfSpeed.cars.models import Car
from worldOfSpeed.profiles.models import Profile


def show_catalogue(request):
    profile = Profile.objects.first()
    cars = Car.objects.all()
    total_cars = cars.count()

    context = {
        'cars': cars,
        'total_cars': total_cars,
        'profile': profile,
    }
    return render(request, 'catalogue.html', context)


def create_car(request):
    profile = Profile.objects.first()

    if request.method == 'POST':

        form = CarForm(request.POST)
        if form.is_valid():
            car = form.save(commit=False)
            car.owner = Profile.objects.first()
            car.save()
            return redirect('catalogue')
    else:
        form = CarForm()

    context = {
        'form': form,
        'profile': profile,
    }
    return render(request, 'car-create.html', context)


def car_details(request, pk):
    profile = Profile.objects.first()
    car = get_object_or_404(Car, pk=pk)

    context = {
        'car': car,
        'profile': profile,
    }
    return render(request, 'car-details.html', context)


def edit_car(request, pk):
    profile = Profile.objects.first()
    car = get_object_or_404(Car, pk=pk)

    if request.method == 'POST':
        form = CarForm(request.POST, instance=car)
        if form.is_valid():
            form.save()
            return redirect('catalogue')
    else:
        form = CarForm(instance=car)

    context = {
        'form': form,
        'profile': profile,
        'car': car,
    }
    return render(request, 'car-edit.html', context)


def delete_car(request, pk):
    profile = Profile.objects.first()
    car = get_object_or_404(Car, pk=pk)

    if request.method == 'POST':
        car.delete()
        return redirect('catalogue')
    else:
        form = DeleteCarForm(instance=car)

    context = {
        'form': form,
        'profile': profile,
        'car': car,
    }

    return render(request, 'car-delete.html', context)
