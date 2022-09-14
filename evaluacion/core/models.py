from tabnanny import verbose
from unicodedata import category
from django.db import models
from django.utils.html import format_html

#Tuplas
group_soccer_team = [
    (1, 'A'),
    (2, 'B'),
    (3, 'C'),
    (4, 'D'),
    (5, 'E'),
    (6, 'F'),
    (7, 'G'),
    (8, 'H'),
]
player_position = [
    (1, 'POR'),
    (2, 'DFC'),
    (3, 'LD'),
    (4, 'LI'),
    (5, 'CAD'),
    (6, 'CAI'),
    (7, 'MCD'),
    (8, 'MD'),
    (9, 'MC'),
    (10, 'MI'),
    (11, 'MCO'),
    (12, 'ED'),
    (13, 'EI'),
    (14, 'DC'),
    (15, 'SD'),
]
rol_technical = [
    (1, 'Técnico'),
    (2, 'Asistente'),
    (3, 'Médico'),
    (4, 'Preparador'),
]

class SoccerTeam(models.Model):
    group = models.IntegerField(verbose_name='Grupo', choices=group_soccer_team)
    name = models.CharField(max_length=50, verbose_name='Nombre')
    flag = models.ImageField('Bandera')
    shield = models.ImageField('Escudo')    

    def bandera(self):
        return format_html ('<img src= {} width="90" height="60" />', self.flag.url)
        
    def escudo(self):
        return format_html ('<img src= {} width="80" height="80" />', self.shield.url)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Selección de fútbol'
        verbose_name_plural = 'Selecciones de fútbol'
        db_table = 'seleccion_futbol'
        ordering = ['group']


class Player(models.Model):
    nationality = models.ForeignKey(SoccerTeam, on_delete=models.CASCADE, verbose_name='Nacionalidad')
    photo = models.ImageField('Foto')
    name = models.CharField(max_length=120, verbose_name='Nombre/s')
    surname = models.CharField(max_length=120, verbose_name='Apellidos')
    date_of_birth = models.DateField(verbose_name='Fecha de nacimiento')
    position = models.IntegerField(verbose_name='Posición', choices=player_position)
    shirt_number = models.IntegerField(verbose_name='Número de camiseta')
    holder = models.BooleanField(verbose_name='¿Es titular?', default=True)

    def foto(self):
        return format_html ('<img src= {} width="80" height="80" />', self.photo.url)

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Jugador'
        verbose_name_plural = 'Jugadores'
        db_table = 'jugador'
        ordering = ['name']

class Technical(models.Model):
    soccer_team = models.ForeignKey(SoccerTeam, on_delete=models.CASCADE, verbose_name='Selección de fútbol')
    photo = models.ImageField('Foto')
    name = models.CharField(max_length=120, verbose_name='Nombre/s')
    surname = models.CharField(max_length=120, verbose_name='Apellidos')
    date_of_birth = models.DateField(verbose_name='Fecha de nacimiento')
    nationality = models.CharField(verbose_name='Nacionalidad(Nombre del país)', max_length=120)
    rol = models.IntegerField(verbose_name='Rol', choices=rol_technical)

    def foto(self):
        return format_html ('<img src= {} width="70" height="100" />', self.photo.url)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Técnico'
        verbose_name_plural = 'Técnicos'
        db_table = 'tecnico'
        ordering = ['rol']

