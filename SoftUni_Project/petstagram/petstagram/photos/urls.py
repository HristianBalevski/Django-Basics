from django.urls import path

from petstagram.photos.views import add_photo, photo_details, edit_page

urlpatterns = [
    path('add/', add_photo, name='add'),
    path('<int:pk>/', photo_details, name='details'),
    path('<int:pk>/edit/', edit_page, name='edit'),
]