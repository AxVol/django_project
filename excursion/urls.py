from django.urls import path

from . import views

app_name = 'excursion'
urlpatterns = [
    path('', views.excursion_view, name = 'excursion_view'),
    path('<int:excursion_id>', views.excursion_detail, name = 'excursion_detail'),
    path('<int:excursion_id>/register_excursion', views.register_excursion, name = 'register_excursion')
]