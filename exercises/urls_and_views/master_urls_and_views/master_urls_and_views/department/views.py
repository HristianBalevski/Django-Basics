from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from master_urls_and_views.department.models import Department


def index(request):

    # return HttpResponse("Hello, world. You're at the polls index.")
    return render(request, 'index.html')


def show_department_by_id(request, department_id):

    department = get_object_or_404(Department, id=department_id)

    return render(request, 'index.html', {'department': department})
