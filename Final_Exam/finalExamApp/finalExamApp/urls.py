
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('finalExamApp.common.urls')),
    path('posts/', include('finalExamApp.posts.urls')),
    path('author/', include('finalExamApp.author.urls')),
]
