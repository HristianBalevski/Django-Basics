
from django.contrib import admin
from django.urls import include, path
from django.conf.urls import handler404

handler404 = 'my_tennis_club.members.views.custom_404'

urlpatterns = [
    path('', include('my_tennis_club.members.urls')),
    path('admin/', admin.site.urls),
]
