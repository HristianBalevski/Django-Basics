from django.urls import path, include

from my_plant.catalogue.views import show_catalogue, create_plant, plant_details, edit_plant, delete_plant

urlpatterns = [
    path('', show_catalogue, name='catalogue'),
    path('create/', create_plant, name='create-plant'),
    path('details/<int:pk>', plant_details, name='plant_details'),
    path('edit/<int:pk>', edit_plant, name='edit_plant'),
    path('delete/<int:pk>', delete_plant, name='delete_plant'),
]