# Generated by Django 4.0.5 on 2022-07-16 11:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0015_articles_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articles',
            name='article_image',
            field=models.FileField(upload_to='articles/'),
        ),
        migrations.AlterField(
            model_name='articles',
            name='author',
            field=models.TextField(),
        ),
    ]
