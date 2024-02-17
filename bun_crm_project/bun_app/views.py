from django.shortcuts import render
from .models import Advertising

def index(request):
    advertising = Advertising.objects.all()
    data = {
        'title': 'Главная страница',
        'advertising': advertising
    }

    return render(request, 'bun_app/index.html', data)


def about(request):
    return render(request, 'bun_app/about.html')




