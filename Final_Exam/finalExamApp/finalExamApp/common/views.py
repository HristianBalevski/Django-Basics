from django.shortcuts import render

from finalExamApp.author.models import Author
from finalExamApp.posts.models import Post


def index(request):
    profile = Author.objects.first()

    content = {
        'profile': profile,
    }
    return render(request, 'index.html', content)


def show_dashboard(request):
    profile = Author.objects.first()
    posts = Post.objects.all()

    for post in posts:
        post.short_content = ' '.join(post.content.split()[:3]) + ('...' if len(post.content.split()) > 3 else '')

    context = {
        'posts': posts,
        'profile': profile,
    }

    return render(request, 'dashboard.html', context)
