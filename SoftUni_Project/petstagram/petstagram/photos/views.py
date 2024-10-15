from django.shortcuts import render


def add_photo(request):
    return render(request, 'photos/photo-add-page.html')


def photo_details(request, pk):
    return render(request, 'photos/photo-details-page.html')


def edit_page(request, pk):
    return render(request, 'photos/photo-edit-page.html')
