
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('my_plant.common.urls')),
    path('profile/', include('my_plant.profiles.urls')),
    path('catalogue/', include('my_plant.catalogue.urls')),
]

