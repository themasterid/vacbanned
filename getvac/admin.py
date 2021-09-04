from django.contrib import admin

from .models import SteamID, SteamInfo, VacInfo


class SteamIDAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'steamid',
        'pub_date',
        'author',
    )
    list_editable = ('steamid',)
    search_fields = ('steamid',)
    list_filter = ('pub_date',)
    empty_value_display = '-пусто-'


class SteamInfoAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'steamid',
        'pub_date',
        'author',
    )
    list_editable = ('steamid',)
    search_fields = ('steamid',)
    list_filter = ('pub_date',)
    empty_value_display = '-пусто-'


class VacInfoAdmin(admin.ModelAdmin):
    list_display = (
        'pk',
        'steamid',
        'pub_date',
        'author',
    )
    list_editable = ('steamid',)
    search_fields = ('steamid',)
    list_filter = ('pub_date',)
    empty_value_display = '-пусто-'


admin.site.register(SteamID, SteamIDAdmin)
admin.site.register(SteamInfo, SteamInfoAdmin)
admin.site.register(VacInfo, VacInfoAdmin)
