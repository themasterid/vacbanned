# posts/views.py
import requests
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render

from .forms import RecordForm, SteamInfoForm, VacInfoForm
from .models import SteamID, SteamInfo, VacInfo

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
    context = {
        'steamids': steamids,
    }
    return render(request, 'getvac/index.html', context)


def post_detail(request, post_id):
    post = get_object_or_404(SteamID, id=post_id)
    steamid = get_object_or_404(SteamID, id=post_id)
    steamids1 = SteamInfo.objects.filter(steamid=steamid)
    vacstatus = VacInfo.objects.filter(steamid=steamid)
    posts_count = SteamID.objects.filter(author=post.author).count()
    template = 'getvac/post_detail.html'
    context = {
        'post': post,
        'posts_count': posts_count,
        'requser': request.user,
        'steamid': steamid,
        'vacstatus': vacstatus,
        'steamids1': steamids1,
        }
    return render(request, template, context)


@login_required
def record_create(request):
    template = 'getvac/record_create.html'
    if request.method == 'GET':
        form = RecordForm(request.POST or None)
        context = {'form': form}
        return render(request, template, context)
    form = RecordForm(request.POST or None)
    steamid = request.POST.get('steamid')
    steam_info = requests.get(f'{GPS}{steamid}').json()
    vacstatus = requests.get(f'{GPB}{steamid}').json()
    data = {
        'steamid':
        steam_info['response']['players'][0].get('steamid', 'None'),
        'communityvisibilitystate':
        steam_info['response']['players'][0].get(
            'communityvisibilitystate', 'None'),
        'profilestate':
        steam_info['response']['players'][0].get('profilestate', 'None'),
        'personaname':
        steam_info['response']['players'][0].get('personaname', 'None'),
        'commentpermission':
        steam_info['response']['players'][0].get('commentpermission', 'None'),
        'profileurl':
        steam_info['response']['players'][0].get('profileurl', 'None'),
        'avatar':
        steam_info['response']['players'][0].get('avatar', 'None'),
        'avatarmedium':
        steam_info['response']['players'][0].get('avatarmedium', 'None'),
        'avatarfull':
        steam_info['response']['players'][0].get('avatarfull', 'None'),
        'avatarhash':
        steam_info['response']['players'][0].get('avatarhash', 'None'),
        'lastlogoff':
        steam_info['response']['players'][0].get('lastlogoff', 'None'),
        'personastate':
        steam_info['response']['players'][0].get('personastate', 'None'),
        'realname':
        steam_info['response']['players'][0].get('realname', 'None'),
        'primaryclanid':
        steam_info['response']['players'][0].get('primaryclanid', 'None'),
        'timecreated':
        steam_info['response']['players'][0].get('timecreated', 'None'),
        'personastateflags':
        steam_info['response']['players'][0].get(
            'personastateflags', 'None'),
        'loccountrycode':
        steam_info['response']['players'][0].get('loccountrycode', 'None'),
        'locstatecode':
        steam_info['response']['players'][0].get('locstatecode', 'None'),
        'loccityid':
        steam_info['response']['players'][0].get('loccityid', 'None'),
    }

    data_vac = {
        'steamid':
        vacstatus['players'][0].get('SteamId', 'None'),
        'CommunityBanned':
        vacstatus['players'][0].get(
            'CommunityBanned', 'None'),
        'VACBanned':
        vacstatus['players'][0].get('VACBanned', 'None'),
        'NumberOfVACBans':
        vacstatus['players'][0].get('NumberOfVACBans', 'None'),
        'DaysSinceLastBan':
        vacstatus['players'][0].get('DaysSinceLastBan', 'None'),
        'NumberOfGameBans':
        vacstatus['players'][0].get('NumberOfGameBans', 'None'),
        'EconomyBan':
        vacstatus['players'][0].get('EconomyBan', 'None'),
    }

    form_info = SteamInfoForm(data)
    form_vac_info = VacInfoForm(data_vac)
    if form.is_valid() and form_info.is_valid() and form_vac_info.is_valid():
        create_post = form.save(commit=False)
        create_post_info = form_info.save(commit=False)
        create_post_vac_info = form_vac_info.save(commit=False)
        create_post.author = request.user
        create_post.save()
        create_post_info.author = request.user
        create_post_info.save()
        create_post_vac_info.author = request.user
        create_post_vac_info.save()
        return redirect('getvac:index')
    form = RecordForm(request.POST or None)
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
