# getvac/forms.py
from django import forms

from .models import SteamID, SteamInfo, VacInfo


class RecordForm(forms.ModelForm):

    def clean_steamid(self):
        data = self.cleaned_data['steamid']
        # ! нет проверки на правильность steamid формата 765611981XXXX
        if (
            len(data) != 17
            or isinstance(data, int)
            or SteamID.objects.filter(steamid__contains=data).exists()
        ):
            raise forms.ValidationError(
                'Введите правильный SteamID (765611982904XXXXX)'
                ' или SteamID есть в базе')
        return data

    class Meta:
        model = SteamID
        fields = ['steamid']
        help_texts = {
            'steamid': 'Введите Steam ID',
        }


class SteamInfoForm(forms.ModelForm):

    class Meta:
        model = SteamInfo
        fields = [
            'steamid',
            'communityvisibilitystate',
            'profilestate',
            'personaname',
            'commentpermission',
            'profileurl',
            'avatar',
            'avatarmedium',
            'avatarfull',
            'avatarhash',
            'lastlogoff',
            'personastate',
            'realname',
            'primaryclanid',
            'timecreated',
            'personastateflags',
            'loccountrycode',
            'locstatecode',
            'loccityid'
        ]
        help_texts = {
            'steamid': 'Введите Steam ID',
        }


class VacInfoForm(forms.ModelForm):

    class Meta:
        model = VacInfo
        fields = [
            'steamid',
            'CommunityBanned',
            'VACBanned',
            'NumberOfVACBans',
            'DaysSinceLastBan',
            'NumberOfGameBans',
            'EconomyBan',
        ]
        help_texts = {
            'steamid': 'Введите Steam ID',
        }
