from django.shortcuts import render, get_object_or_404


def home_page(request):
    return render(request, 'common/home-page.html')


def register_page(request):
    return render(request, 'accounts/register-page.html')


def login_page(request):
    return render(request, 'accounts/login-page.html')


def profile_details(request, pk):
    return render(request, 'accounts/profile-details-page.html')


def edit_profile(request, pk):
    return render(request, 'accounts/profile-edit-page.html')


def delete_profile(request, pk):
    return render(request, 'accounts/profile-delete-page.html')


def add_pet(request):
    return render(request, 'pets/pet-add-page.html')


def edit_pet(request, username, pet_slug):
    return render(request, 'pets/pet-edit-page.html')