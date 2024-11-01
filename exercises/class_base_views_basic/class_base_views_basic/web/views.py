from random import random

from django.http import HttpResponseNotAllowed
from django.shortcuts import render
from django.views import View


def perform_always():
    pass


class BaseView(View):
    def dispatch(self, request, *args, **kwargs):
        perform_always()  # We only have to inherit our class, the chance for human mistake is lower!

        return super().dispatch(request, *args, **kwargs)


def index(request):
    perform_always()  # We have to invoke the function all the time, the chance for human mistake is higher!

    if request.method == 'POST':
        # perform post logic
        pass
    else:
        # perform get logic
        pass

    return render(request, 'index.html')


class IndexView(View):
    def dispatch(self, request, *args, **kwargs):
        # check permissions of user
        # if random() < 0.5:
        #     return HttpResponseNotAllowed(['get'])

        return super().dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        # perform get logic
        return render(request, 'index.html')

    def post(self, request):
        # perform post logic
        pass
