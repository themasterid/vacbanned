# posts/views.py
from django.shortcuts import render

from .models import SteamID


def index(request):
    steamids = SteamID.objects.all()[:10]
    context = {
        'steamids': steamids,
    }
    return render(request, 'getvac/index.html', context)


def get_vac_status(steam):
    lists = []
    for i in range(len(steam)):
        lists.append(steam[i].steam)
    return lists
