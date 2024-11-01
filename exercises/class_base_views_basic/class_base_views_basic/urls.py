
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('class_base_views_basic.web.urls')),
    path('custom/', include('class_base_views_basic.custom_class_base_views.urls')),
]
