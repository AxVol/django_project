# Generated by Django 4.0.5 on 2022-07-17 11:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('excursion', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='excursions',
            name='reg_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
