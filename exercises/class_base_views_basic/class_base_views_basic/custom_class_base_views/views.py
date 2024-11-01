import time
from datetime import datetime

from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views import generic as views
from django.views.generic import TemplateView, CreateView, DetailView

from class_base_views_basic.web.forms import TodoBaseForm
from class_base_views_basic.web.models import Todo


class BaseView:
    @classmethod
    def as_view(cls):
        def view(request, *args, **kwargs):
            self = cls()
            # self is instance of the current class.
            # BaseView.as_view() -> cls = BaseView
            # IndexView.as_view() -> cls = IndexView

            if request.method == "GET":
                return self.get(request, *args, **kwargs)
            else:
                return self.post(request, *args, **kwargs)

        return view


class IndexView(BaseView):
    def get(self, request):
        return HttpResponse('It works with Class Base View')


def index(request):
    return HttpResponse('It works with Function Base View')


class IndexTemplateView(TemplateView):
    template_name = 'index.html'

    # 'context' with static data, i.e no DB calls
    extra_context = {
        'title': 'With extra context',
        'static_time': datetime.now()
    }

    # 'context' with dynamic data, i.e DB calls
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['dynamic_time'] = datetime.now()
        context['todo_list'] = Todo.objects.all()

        return context


class TodoCreateView(CreateView):
    model = Todo
    fields = '__all__'
    template_name = 'create_todo.html'

    # Static way
    # success_url = reverse_lazy('index')

    # Dynamic way
    def get_success_url(self):
        return reverse('todo-details', kwargs={'pk': self.object.pk})

    # Static way
    # form_class = TodoBaseForm

    # Dynamic way
    def get_form_class(self):
        # return TodoBaseForm
        return super().get_form_class()

    def get_form(self, form_class=None):
        return super().get_form(form_class=form_class)


class DetailsView(DetailView):
    model = Todo
    template_name = 'todo_details.html'
