from django.db import models
from django.utils import timezone

import datetime

class Articles(models.Model):
    author = models.TextField()
    caption_name = models.CharField(max_length = 50)
    caption_mini_text = models.CharField(max_length = 200)
    articles_text = models.TextField(max_length = 2000)
    count_comm = models.IntegerField(default = 0)
    pub_date = models.DateTimeField('date published', default  = timezone.now)
    article_image = models.FileField(upload_to = 'articles/')

    rank = [
        ('Blog', 'Blog'),
        ('History', 'History'),
        ('Facts', 'Facts'),
        ('Guide', 'Guide')
    ]

    ranks = models.CharField(max_length = 10, choices = rank, default = 'Blog')

class Comments(models.Model):
    articles = models.ForeignKey(Articles, on_delete = models.CASCADE)
    author = models.TextField()
    comment_text = models.TextField()
    pub_date = models.DateTimeField('date published', default = timezone.now)

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days = 1)