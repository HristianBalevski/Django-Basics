from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Member


def members(request):
    # template = loader.get_template('myfirst.html')
    # return HttpResponse(template.render())

    my_members = Member.objects.all()
    context = {'my_members': my_members}

    return render(request, 'all_members.html', context)


def details(request, slug):
    member = Member.objects.get(slug=slug)
    context = {'member': member}

    return render(request, 'details.html', context)


def main(request):
    return render(request, 'main.html')


def custom_404(request, exception):
    return render(request, '404.html', status=404)


def testing(request):
    # Member.objects.values() or all(), Member.objects.values_list(), Member.objects.filter(first_name='Name').values()
    # Member.objects.filter(first_name='Emil').values() | Member.objects.filter(first_name='Tobias').values()
    # Member.objects.filter(last_name='Refsnes', id=2).values()
    # Member.objects.filter(first_name__startswith='L')

    my_members = Member.objects.all().order_by('last_name', '-id').values()
    context = {
        'my_members': my_members,
    }
    return render(request, 'template.html', context)


def fruits(request):
    context = {
        'fruits': ['Apple', 'Banana', 'Cherry']
    }

    return render(request, 'fruits.html', context)