# Generated by Django 4.0.5 on 2022-07-07 18:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0003_articles_caption_img'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.TextField()),
                ('comment_text', models.TextField()),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
                ('name_article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='articles.articles')),
            ],
        ),
        migrations.DeleteModel(
            name='Coments',
        ),
    ]
