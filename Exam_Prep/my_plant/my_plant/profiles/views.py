from django.shortcuts import render, redirect

from my_plant.catalogue.models import Plant
from my_plant.profiles.forms import CreateProfileForm, EditProfileForm
from my_plant.profiles.models import Profile


def create_profile(request):
    if request.method == 'POST':
        form = CreateProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('catalogue')
    else:
        form = CreateProfileForm()

    context = {
        'form': form,
    }

    return render(request, 'create-profile.html', context)


def profile_details(request):
    plants_count = Plant.objects.count()
    profile = Profile.objects.first()

    context = {
        'profile': profile,
        'plants_count': plants_count,
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
    }
    return render(request, 'edit-profile.html', context)


def delete_profile(request):
    profile = Profile.objects.first()
    plants = Plant.objects.all()

    if request.method == 'POST':

        plants.delete()
        profile.delete()
        return redirect('home_page')

    context = {
        'profile': profile,
    }

    return render(request, 'delete-profile.html', context)

