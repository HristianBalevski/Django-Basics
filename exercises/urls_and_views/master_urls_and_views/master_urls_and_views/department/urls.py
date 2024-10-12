from django.urls import path

from master_urls_and_views.department.views import index, show_department_by_id

urlpatterns = [
    path('', index),
    path('department/<int:department_id>/', show_department_by_id),
]