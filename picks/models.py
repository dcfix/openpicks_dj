from django.db import models
from django.conf import settings

class Team(models.Model):
    city = models.CharField(max_length=50)
    team_name = models.CharField(max_length=50)
    icon = models.CharField(max_length=100) # the path to the icon

class Game(models.Model):
    week = models.IntegerField()
    home_team_id = models.ForeignKey(Team, null=False, on_delete=models.PROTECT,
                                     related_name="home_team")
    away_team_id = models.ForeignKey(Team, null=False, on_delete=models.PROTECT,
                                     related_name="away_team")
    game_date = models.DateTimeField()
    tie_breaker = models.BooleanField(default=False)
    final_score_home = models.IntegerField(default=0)
    final_score_away = models.IntegerField(default=0)

class Pick(models.Model):
    picker_id = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)
    game_id = models.ForeignKey(Game, null=False, on_delete=models.PROTECT)
    home_score = models.IntegerField(default=0)
    away_score = models.IntegerField(default=0)
    win = models.IntegerField(default=0)