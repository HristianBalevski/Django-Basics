from django.shortcuts import render, redirect, get_object_or_404

from finalExamApp.author.models import Author
from finalExamApp.posts.forms import PostForm, DeletePostForm
from finalExamApp.posts.models import Post


def create_post(request):
    profile = Author.objects.first()

    if request.method == 'POST':
        form = PostForm(request.POST)

        if form.is_valid():
            post = form.save(commit=False)
            post.author = profile
            post.save()
            return redirect('show_dashboard')
    else:
        form = PostForm()

    context = {'form': form,
               'profile': profile
               }

    return render(request, 'create-post.html', context)


def post_details(request, pk):
    profile = Author.objects.first()
    post = get_object_or_404(Post, pk=pk)

    context = {
        'post': post,
        'profile': profile
    }
    return render(request, 'details-post.html', context)


def edit_post(request, pk):
    profile = Author.objects.first()
    post = get_object_or_404(Post, pk=pk)

    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('show_dashboard')
    else:
        form = PostForm(instance=post)

    context = {
        'form': form,
        'profile': profile,
        'post': post
    }
    return render(request, 'edit-post.html', context)


def delete_post(request, pk):
    profile = Author.objects.first()
    post = get_object_or_404(Post, pk=pk)

    if request.method == 'POST':
        post.delete()
        return redirect('show_dashboard')
    else:
        form = DeletePostForm(instance=post)

    context = {
        'form': form,
        'profile': profile,
        'post': post
    }
    return render(request, 'delete-post.html', context)
