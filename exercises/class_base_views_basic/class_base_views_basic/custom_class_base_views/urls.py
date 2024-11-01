from django.urls import path

from class_base_views_basic.custom_class_base_views.views import IndexView, index, IndexTemplateView, TodoCreateView, \
    DetailsView

urlpatterns = [
    path('', index, name='index'),
    path('template/', IndexTemplateView.as_view(), name='index-template'),
    path('cbv/', IndexView.as_view(), name='index-cbv'),
    path('todos/create/', TodoCreateView.as_view(), name='todo-create'),
    path('todos/<int:pk>/', DetailsView.as_view(), name='todo-details'),
]