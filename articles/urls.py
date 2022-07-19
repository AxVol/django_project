from django.urls import path

from . import views

app_name = 'articles'
urlpatterns = [
    path('', views.articles, name = 'articles'),
    path('<int:articles_id>', views.article_detail, name = 'article_detail')
]
