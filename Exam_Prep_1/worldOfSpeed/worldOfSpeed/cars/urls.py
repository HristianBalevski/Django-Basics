from django.urls import path
from worldOfSpeed.cars.views import show_catalogue, create_car, car_details, edit_car, delete_car

urlpatterns = [
    path('catalogue/', show_catalogue, name='catalogue'),
    path('create/', create_car, name='create_car'),
    path('<int:pk>/details/', car_details, name='car_details'),
    path('<int:pk>/edit/', edit_car, name='edit_car'),
    path('<int:pk>/delete/', delete_car, name='delete_car'),
]
