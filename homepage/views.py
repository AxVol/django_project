from django.shortcuts import render

from articles.models import Articles
from excursion.models import Excursions

from random import randrange

import pycountry

# Функция отвечающая за поиск статей и экскурсий на сайте, а так же по их фильтру в соответствующих блоках
def searching(rank, filter_article = [], filter_excursion = []):
    filter = []
    Efilter = []

    """ 
    Идет перебор полученных объектов статей или экскурсий, после чего добавляет их в список который передается 
    контекстом на страницу, а там уже на основе полученных данных в HTML-странцие выводяться нужные поля
    """

    for filters in filter_article:
        # Этот блок if отвечает за форму фильтра на странице со всеми статьями
        if filters.ranks == rank:
            filter.append(filters)
        # это условия, для формы поиска статей по всему сайту
        elif rank.lower() in filters.caption_name.lower():
            filter.append(filters)

    #Такой же блок для экскурсий
    for filters in filter_excursion:
        if filters.ranks == rank:
            Efilter.append(filters)
        elif rank.lower() in filters.caption_name.lower():
            Efilter.append(filters)
        
    context = {
        'index_articles':filter,
        'index_excursion':Efilter
    }

    if (len(filter) == 0) and (len(Efilter) == 0):
        context = {
            'not_found':"Article not found"
        }

    return context

# Отрисовка главной страницы сайта
def home(request):
    last_articles = Articles.objects.order_by("-pub_date")[:3]
    popular_articles = Articles.objects.order_by("-count_comm")[:3]
    search_articles = Articles.objects.all()
    
    country = []
    counter = 0

    #Блок отвечающий за наполнения опроса "в каких странах вы хотели бы побывать?"
    #Выводящий 5 различных вариантов
    for i in range(len(pycountry.countries)):
        for j in pycountry.countries:
            rand = randrange(1, len(pycountry.countries))

            if i == rand:
                if counter <= 4:
                    counter += 1
                    country.append(j.name)

    context = {
        'last_articles':last_articles,
        'popular_articles':popular_articles,
        'country':country
    }

    if request.method == "POST":
        if request.POST.get('search'):
            return render(request, 'articles/articles.html', searching(request.POST.get('search'), search_articles))

    return render(request, 'articles/index.html', context)

# Отрисовка страницы на которую идет редирект при поиске с выдачей всех вариантов
def search(request):
    index_articles = Articles.objects.all()
    index_excursion = Excursions.objects.all()

    if request.method == "GET":
        if request.GET.get('search'):
            return render(request, 'homepage/search.html', searching(request.GET.get('search'), index_articles, index_excursion))