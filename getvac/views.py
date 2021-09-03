# posts/views.py
import requests
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render

from .forms import RecordForm
from .models import SteamID

KEY = settings.CODES['key']
GPS = (
    'https://api.steampowered.com/ISteamUser/'
    f'GetPlayerSummaries/v2/?key={KEY}&steamids='
)

GUSFG = (
    'https://api.steampowered.com/ISteamUserStats/'
    'GetUserStatsForGame/v0002/'
    f'?appid=730&key={KEY}&steamid='
)

GPB = (
    'https://api.steampowered.com/ISteamUser/'
    f'GetPlayerBans/v1/?key={KEY}&steamids='
)


def index(request):
    steamids = SteamID.objects.all()
    context = {'steamids': steamids, }
    return render(request, 'getvac/index.html', context)


def info(request, post_id):
    steamid = get_object_or_404(SteamID, id=post_id)
    steamid_status = requests.get(f'{GPS}{steamid}').json()
    vacstatus = get_vac_status(steamid)
    template = 'includes/info.html'
    context = {
        'steamid': steamid,
        'steamid_status': steamid_status,
        'vacstatus': vacstatus,
    }
    return render(request, template, context)


def get_vac_status(steamid):
    return requests.get(f'{GPB}{steamid}').json()


def post_detail(request, post_id):
    post = get_object_or_404(SteamID, id=post_id)
    steamid = get_object_or_404(SteamID, id=post_id)
    steamid_status = requests.get(f'{GPS}{steamid}').json()
    vacstatus = get_vac_status(steamid)
    posts_count = SteamID.objects.filter(author=post.author).count()
    template = 'getvac/post_detail.html'
    context = {
        'post': post,
        'posts_count': posts_count,
        'requser': request.user,
        'steamid': steamid,
        'steamid_status': steamid_status,
        'vacstatus': vacstatus,
        }
    return render(request, template, context)


@login_required
def record_create(request):
    form = RecordForm(request.POST or None)
    if form.is_valid():
        create_post = form.save(commit=False)
        create_post.author = request.user
        create_post.save()
        return redirect('getvac:ok')
    template = 'getvac/record_create.html'
    context = {'form': form}
    return render(request, template, context)


@login_required
def post_edit(request, post_id):
    edit_post = get_object_or_404(SteamID, id=post_id)
    if request.user != edit_post.author:
        return redirect('getvac:post_detail', post_id)
    form = RecordForm(request.POST or None, instance=edit_post)
    if form.is_valid():
        form.save()
        return redirect('getvac:post_detail', post_id)
    template = 'getvac/record_create.html'
    context = {'form': form}
    return render(request, template, context)


def go_ok(request):
    return render(request, 'getvac/ok.html')
