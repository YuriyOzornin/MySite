from django.shortcuts import render

# Create your views here.

from .models import New

def home(request):
    data = {
        'news': New.objects.all(),
        'title': 'Главная страница'
    }
    return render(request, 'blog/home.html', data)


def contacts(request):
    return render(request, 'blog/contacts.html', {'title': 'english_ekb_online'})
