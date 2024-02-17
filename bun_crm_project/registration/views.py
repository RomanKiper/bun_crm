from django.shortcuts import render


def registration(request):
    data = {
        'registration_data': 'Страница регистарции'
    }
    return render(request, 'registration/registration.html', data)


