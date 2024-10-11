from django.contrib import admin
from django.urls import path, include
from learnBasics.quieroAprender import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('learnBasics.quieroAprender.urls')),
]
