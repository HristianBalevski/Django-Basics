from django.urls import path

from petstagram.pets.views import add_pet, pet_details, edit_pet, delete_pet

urlpatterns = [
    path('add/', add_pet, name='add_pet'),
    path('<str:username>/pet/<slug:slug_pet>/', pet_details, name='pet_details'),
    path('<str:username>/pet/<slug:slug_pet>/edit/', edit_pet, name='edit_pet'),
    path('<str:username>/pet/<slug:slug_pet>/delete/', delete_pet, name='delete_pet'),
]