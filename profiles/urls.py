from django.urls import path

from . import views

app_name = 'profiles'
urlpatterns = [
    path('', views.cabinet, name = 'cabinet'),
    path('create_article/', views.create_article, name = 'create_article')
]