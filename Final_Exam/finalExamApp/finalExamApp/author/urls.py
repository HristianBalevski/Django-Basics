from django.urls import path

from finalExamApp.author.views import create_author, author_details, edit_author, delete_author

urlpatterns = [
    path('create/', create_author, name='create-author'),
    path('details/', author_details, name='author-details'),
    path('edit/', edit_author, name='author-edit'),
    path('delete/', delete_author, name='author-delete'),
]