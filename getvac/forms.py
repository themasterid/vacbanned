# getvac/forms.py
from django import forms

from .models import SteamID


class RecordForm(forms.ModelForm):

    class Meta:
        model = SteamID
        fields = ['steamid']
        help_texts = {
            'steamid': 'SteamID ... ',
        }
