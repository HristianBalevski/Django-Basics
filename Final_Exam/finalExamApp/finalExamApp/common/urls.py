from django.urls import path

from finalExamApp.common.views import index, show_dashboard

urlpatterns = [
    path('', index, name='index'),
    path('dashboard/', show_dashboard, name='show_dashboard'),
]