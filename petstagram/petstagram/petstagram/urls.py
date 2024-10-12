
from django.contrib import admin
from django.urls import path, include

import petstagram
from petstagram.petsApp.views import home_page

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('petstagram.petsApp.urls')),
]
