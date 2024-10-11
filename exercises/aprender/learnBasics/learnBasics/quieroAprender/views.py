from django.shortcuts import render


def index(request):
    context = {
        'languages': {
            'english': 'English',
            'spanish': 'Spanish',
        }
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
        }
    }

    return render(request, 'languages.html', context)


