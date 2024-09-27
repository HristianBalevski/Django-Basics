from django.urls import path, include
from petstagram.photos import views

urlpatterns = (
    path('', views.add_photo, name='add-photo'),
    path('<int:pk>/', include([
        path('photo/', views.photo_details, name='photo-details'),
        path('edit/', views.edit_photo, name='photo-edit'),
    ]))
)