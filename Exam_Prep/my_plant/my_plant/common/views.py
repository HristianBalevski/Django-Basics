from django.shortcuts import render

from my_plant.profiles.models import Profile


def home_page(request):
    profile = Profile.objects.first()

    context = {
        'profile': profile,
    }
    return render(request, 'home-page.html', context)
