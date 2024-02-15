from django.shortcuts import render

def index(request):
    data = {
        'title': 'Главная страница '
    }
    return render(request, 'bun_app/index.html', data)


def about(request):
    return render(request, 'bun_app/about.html')

