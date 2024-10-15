from django.urls import path

from petstagram.accounts.views import register_user, login_user, profile_details, edit_profile, delete_profile

urlpatterns = [
    path('register/', register_user, name='register'),
    path('login/', login_user, name='login'),
    path('profile/<int:pk>/', profile_details, name='profile'),
    path('profile/<int:pk>/edit/', edit_profile, name='edit_profile'),
    path('profile/<int:pk>/delete/', delete_profile, name='delete_profile'),


]