from django.shortcuts import render, redirect
from learnBasics.quieroAprender.models import Post
from learnBasics.quieroAprender.forms import PersonForm, PostForm, DeletePost


def index(request):
    # context = {
    #     'languages': {
    #         'english': 'English',
    #         'spanish': 'Spanish',
    #     }
    # }
    form = PersonForm(request.POST or None)

    if request.method == 'POST':
        print(request.POST['person_name'])

    if form.is_valid():
        print(form.cleaned_data['person_name'])

    context = {
        'my_form': form,
    }

    return render(request, 'home-page.html', context)


def learn_language(request):
    context = {
        'english': {
            'title': 'Welcome to our English lessons',
            'lessons': {
                'lesson_one': 'Describing personality traits',
                'lesson_two': 'Feelings and emotions',
                'lesson_three': 'Ecology and environment',
            }
        },

        'spanish': {
            'title': 'Welcome to our Spanish Lessons',
            'lessons': {
                'lesson_one': 'Los adverbios.',
                'lesson_two': 'El artículo.',
                'lesson_three': 'Tipos de palabras.',
            }
        },

        'new_posts': Post.objects.all(),

    }

    return render(request, 'languages.html', context)


def add_post(request):
    form = PostForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('languages')

    context = {
        'form': form,
    }

    return render(request, 'add-post.html', context)


def delete_post(request, pk: int):
    post = Post.objects.get(pk=pk)
    form = DeletePost(instance=post)

    if request.method == 'POST':
        post.delete()
        return redirect('languages')

    context = {
        'form': form,
        'post': post,
    }

    return render(request, 'delete-template.html', context)


def details_page(request, pk: int):
    post = Post.objects.get(pk=pk)

    context = {
        'post': post,
    }

    return render(request, 'details-post.html', context)