from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class SteamID(models.Model):
    steamid = models.CharField(max_length=17, verbose_name='SteamID')
    vac_status = models.CharField(max_length=200, verbose_name='VAC STATUS')
    pub_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата')
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='Автор'
    )

    def __str__(self):
        return self.steamid

    class Meta:
        ordering = ('pub_date',)
        verbose_name_plural = 'SteamID`s'
        verbose_name = 'SteamID'
