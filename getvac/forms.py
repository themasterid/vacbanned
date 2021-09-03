# getvac/forms.py
from django import forms

from .models import SteamID


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
