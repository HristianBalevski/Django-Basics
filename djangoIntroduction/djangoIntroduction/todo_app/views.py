from django.shortcuts import render
from django.http import HttpResponse
from


def index(request):

    tasks = Task.objects.all()
    context = {'tasks': tasks}

    return render(request, 'tasks/index.html', context)

