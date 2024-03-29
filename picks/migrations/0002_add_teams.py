# Generated by Django 4.1.7 on 2023-03-02 01:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('picks', '0001_initial'),
    ]

    operations = [
        migrations.RunSQL(
            """insert into picks_team(city, team_name, icon) values
        ('Minnesota', 'Vikings', 'MIN'),
        ('Cleveland', 'Browns', 'CLE'),
        ('Atlanta', 'Falcons', 'ATL'),
        ('Cincinnati', 'Bengals', 'CIN'),
        ('New York Jets', 'Jets', 'NYJ'),
        ('Houston', 'Texans', 'HOU'),
        ('Green Bay', 'Packers', 'GB'),
        ('Denver', 'Broncos', 'DEN'),
        ('Chicago', 'Bears', 'CHI'),
        ('Baltimore', 'Ravens', 'BAL'),
        ('New York Giants', 'Giants', 'NYG'),
        ('Kansas City', 'Chiefs', 'KC'),
        ('Detroit', 'Lions', 'DET'),
        ('Philadelphia', 'Eagles', 'PHI'),
        ('Tennessee', 'Titans', 'TEN'),
        ('New', 'Orleans', 'Saints	NO'),
        ('Dallas', 'Cowboys', 'DAL'),
        ('Tampa Bay', 'Buccaneers', 'TB'),
        ('New England', 'Patriots', 'NE'),
        ('Miami', 'Dolphins', 'MIA'),
        ('Buffalo', 'Bills', 'BUF'),
        ('Seattle', 'Seahawks', 'SEA'),
        ('Carolina', 'Panthers', 'CAR'),
        ('Indianapolis', 'Colts', 'IND'),
        ('Arizona', 'Cardinals', 'ARI'),
        ('Pittsburgh', 'Steelers', 'PIT'),
        ('San Francisco', '49ers', 'SF'),
        ('Jacksonville', 'Jaguars', 'JAX'),
        ('LA Chargers', 'Chargers', 'LAC'),
        ('Washington', 'Commanders', 'WSH'),
        ('Las Vegas', 'Raiders', 'LV'),
        ('LA Rams', 'Rams', 'LAR');"""
        )
    ]
