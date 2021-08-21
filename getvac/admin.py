from django.contrib import admin

from .models import SteamID


class SteamIDAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'steamid',
        'vac_status',
        'pub_date',
        'author',
    )
    list_editable = ('steamid',)
    search_fields = ('steamid',)
    list_filter = ('pub_date',)
    empty_value_display = '-пусто-'


admin.site.register(SteamID, SteamIDAdmin)
