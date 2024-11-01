from django.urls import path

from class_base_views_basic.web.views import index, IndexView

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('<int:pk>/', IndexView.as_view(), name='index'),
]