from django.urls import path, include

from learnBasics.quieroAprender.views import index, learn_language, add_post, delete_post

urlpatterns = [
    path('', index, name='home'),
    path('languages/', learn_language, name='languages'),
    path('add-post/', add_post, name='add-post'),
    path('<int:pk>/', include([
        path('delete-post/', delete_post, name='delete-post'),
    ]))
]
