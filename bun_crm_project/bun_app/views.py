from django.shortcuts import render

def index(request):
    return render(request, 'bun_app/index.html')


def about(request):
    return render(request, 'bun_app/about.html')

