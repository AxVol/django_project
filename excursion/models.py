from django.db import models
from django.contrib.auth.models import User

class Excursions(models.Model):
    caption_name = models.CharField(max_length = 50, default = "Название")
    caption_mini_text = models.CharField(max_length = 200, default = "Описание")
    duraction_in_hour = models.IntegerField(default = 0)
    date_ex = models.TextField(default = "Даты проведения в виде 'число.месяц' ")
    time_ex = models.TextField(default = "Время начала")
    price = models.IntegerField(default = 0)
    registred = models.IntegerField(default = 0)
    place = models.IntegerField(default = 30)
    excursion_image = models.FileField(upload_to = 'excursion/', default = 'None')

    rank = [
        ('Streets', 'Streets'),
        ('Historical', 'Historical'),
        ('Buildings', 'Buildings'),
    ]
    ranks = models.CharField(max_length = 10, choices = rank, default = 'Streets')

class Reg_Excursion(models.Model):
    reg_user = models.ForeignKey(User, on_delete = models.CASCADE)
    reg_excursion = models.ForeignKey(Excursions, on_delete = models.CASCADE)
    reg_date = models.TextField(default = 0)
    reg_people = models.IntegerField(default = 1)