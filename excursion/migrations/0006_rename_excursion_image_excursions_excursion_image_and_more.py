# Generated by Django 4.0.5 on 2022-07-17 11:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('excursion', '0005_excursions_excursion_image_excursions_rank_articles'),
    ]

    operations = [
        migrations.RenameField(
            model_name='excursions',
            old_name='Excursion_image',
            new_name='excursion_image',
        ),
        migrations.RenameField(
            model_name='excursions',
            old_name='rank_articles',
            new_name='rank_excursion',
        ),
    ]
