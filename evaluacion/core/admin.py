from django.contrib import admin
from .models import SoccerTeam, Player, Technical

@admin.register(SoccerTeam)
class SoccerTeamAdmin(admin.ModelAdmin):
    list_display = ("group", "name", "bandera", "escudo")
    list_filter = ["group"]



@admin.register(Player)
class PlayerAdmin(admin.ModelAdmin):
    list_display = ("foto", "name", "surname", "position", "holder")
    list_editable = ("holder",)
    list_filter = ["position", "nationality"]

@admin.register(Technical)
class TachnicalAdmin(admin.ModelAdmin):
    list_display = ("foto", "name", "surname", "nationality", "rol")
    list_filter = ["rol", "soccer_team"]

    