from django.shortcuts import render, redirect
from worldOfSpeed.profiles.forms import ProfileForm, EditProfileForm
from worldOfSpeed.profiles.models import Profile


def create_profile(request):

    if request.method == 'POST':
        form = ProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('catalogue')
    else:
        form = ProfileForm()

    context = {
        'form': form,
    }

    return render(request, 'profile-create.html', context)


def profile_details(request):

    profile = Profile.objects.first()
    total_cars = profile.cars.count()
    total_cars_price = sum([price.price for price in profile.cars.all()])

    context = {
        'profile': profile,
        'total_cars': total_cars,
        'total_cars_price': total_cars_price,
    }
    return render(request, 'profile-details.html', context)


def edit_profile(request):
    profile = Profile.objects.first()

    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profile_details')
    else:
        form = EditProfileForm(instance=profile)

    context = {
        'form': form,
        'profile': profile,
    }
    return render(request, 'profile-edit.html', context)


def delete_profile(request):
    profile = Profile.objects.first()

    if request.method == 'POST':
        profile.cars.all().delete()
        profile.delete()
        return redirect('index')

    context = {
        'profile': profile,
    }
    return render(request, 'profile-delete.html', context)
