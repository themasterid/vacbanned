from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class SteamID(models.Model):
    id = models.AutoField(primary_key=True)
    steamid = models.CharField(
        max_length=17,
        verbose_name='SteamID'
    )
    pub_date = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Дата'
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='Автор'
    )

    class Meta:
        ordering = ('pub_date',)
        verbose_name_plural = 'SteamID`s'
        verbose_name = 'SteamID'

    def __str__(self):
        return self.steamid


class SteamInfo(models.Model):
    id = models.AutoField(primary_key=True)
    steamid = models.CharField(
        max_length=200, verbose_name='steamid')
    communityvisibilitystate = models.CharField(
        max_length=200, verbose_name='communityvisibilitystate')
    profilestate = models.CharField(
        max_length=200, verbose_name='profilestate')
    personaname = models.CharField(
        max_length=200, verbose_name='personaname')
    commentpermission = models.CharField(
        max_length=200, verbose_name='commentpermission')
    profileurl = models.CharField(
        max_length=200, verbose_name='profileurl')
    avatar = models.CharField(
        max_length=200, verbose_name='avatar')
    avatarmedium = models.CharField(
        max_length=200, verbose_name='avatarmedium')
    avatarfull = models.CharField(
        max_length=200, verbose_name='avatarfull')
    avatarhash = models.CharField(
        max_length=200, verbose_name='avatarhash')
    lastlogoff = models.CharField(
        max_length=200, verbose_name='lastlogoff')
    personastate = models.CharField(
        max_length=200, verbose_name='personastate')
    realname = models.CharField(
        max_length=200, verbose_name='realname')
    primaryclanid = models.CharField(
        max_length=200, verbose_name='primaryclanid')
    timecreated = models.CharField(
        max_length=200, verbose_name='timecreated')
    personastateflags = models.CharField(
        max_length=200, verbose_name='personastateflags')
    loccountrycode = models.CharField(
        max_length=200, verbose_name='loccountrycode')
    locstatecode = models.CharField(
        max_length=200, verbose_name='locstatecode')
    loccityid = models.CharField(
        max_length=200, verbose_name='loccityid')
    pub_date = models.DateTimeField(
        auto_now_add=True, verbose_name='Дата')
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='Автор'
    )

    class Meta:
        ordering = ('pub_date',)
        verbose_name_plural = 'SteamInfo`s'
        verbose_name = 'SteamInfo'

    def __str__(self):
        return self.steamid


class VacInfo(models.Model):
    id = models.AutoField(primary_key=True)
    steamid = models.CharField(
        max_length=200, verbose_name='steamid')
    CommunityBanned = models.CharField(
        max_length=200, verbose_name='CommunityBanned')
    VACBanned = models.CharField(
        max_length=200, verbose_name='VACBanned')
    NumberOfVACBans = models.CharField(
        max_length=200, verbose_name='NumberOfVACBans')
    DaysSinceLastBan = models.CharField(
        max_length=200, verbose_name='DaysSinceLastBan')
    NumberOfGameBans = models.CharField(
        max_length=200, verbose_name='NumberOfGameBans')
    EconomyBan = models.CharField(
        max_length=200, verbose_name='EconomyBan')
    pub_date = models.DateTimeField(
        auto_now_add=True, verbose_name='Дата')
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='Автор'
    )

    class Meta:
        ordering = ('pub_date',)
        verbose_name_plural = 'VacInfo`s'
        verbose_name = 'VacInfo'

    def __str__(self):
        return self.steamid
