from django.urls import path

from finalExamApp.posts.views import create_post, post_details, edit_post, delete_post

urlpatterns = [
    path('create/', create_post, name='create_post'),
    path('<int:pk>/details/', post_details, name='post_details'),
    path('<int:pk>/edit/', edit_post, name='edit_post'),
    path('<int:pk>/delete/', delete_post, name='delete_post'),
]