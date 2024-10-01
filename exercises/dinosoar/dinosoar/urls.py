
from django.contrib import admin
from django.urls import path

from dinofacts.views import show_dino

urlpatterns = [
    path('admin/', admin.site.urls),
    path("show_dino/<str:name>/", show_dino),
]
