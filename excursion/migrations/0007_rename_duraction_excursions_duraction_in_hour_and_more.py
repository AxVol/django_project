# Generated by Django 4.0.5 on 2022-07-17 13:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('excursion', '0006_rename_excursion_image_excursions_excursion_image_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='excursions',
            old_name='duraction',
            new_name='duraction_in_hour',
        ),
        migrations.AlterField(
            model_name='excursions',
            name='place',
            field=models.IntegerField(default=30),
        ),
    ]
