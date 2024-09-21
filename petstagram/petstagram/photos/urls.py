from django.urls import path, include
from petstagram.photos import views

urlpatterns = (
    path('photos/', views.add_photo, name='add-photo'),
    path('photos/<int:pk>/', include([
        path('', views.photo_details, name='photo-details'),
        path('edit/', views.edit_photo, name='photo-edit'),
    ]))
)