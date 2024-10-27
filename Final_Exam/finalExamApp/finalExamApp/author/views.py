from django.shortcuts import render, redirect
from finalExamApp.author.forms import AuthorForm, EditAuthorForm
from finalExamApp.author.models import Author


def create_author(request):
    if request.method == 'POST':

        form = AuthorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('show_dashboard')
    else:
        form = AuthorForm()

    context = {
        'form': form
    }
    return render(request, 'create-author.html', context)


def author_details(request):
    profile = Author.objects.first()
    published_posts = profile.posts.count()
    posts = profile.posts.all()
    last_post = posts.order_by('-updated_at').first()

    context = {
        'profile': profile,
        'published_posts': published_posts,
        'last_post': last_post,
    }
    return render(request, 'details-author.html', context)


def edit_author(request):
    profile = Author.objects.first()

    if request.method == 'POST':
        form = EditAuthorForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('author-details')
    else:
        form = EditAuthorForm(instance=profile)

    context = {
        'form': form,
        'profile': profile
    }

    return render(request, 'edit-author.html', context)


def delete_author(request):
    profile = Author.objects.first()
    if request.method == 'POST':
        profile.posts.all().delete()
        profile.delete()
        return redirect('index')

    context = {
        'profile': profile
    }
    return render(request, 'delete-author.html', context)