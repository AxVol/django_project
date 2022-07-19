from django.shortcuts import render

from articles.models import Articles
from excursion.models import Excursions, Reg_Excursion

# Отображение контента в кабинете
def render_cabinet(name, articles, excursions, reg_excursions):
    article = []
    excursion = []
    reg_excursion = []
    
    for i in articles:
        if i.author == name.username:
            article.append(i)   

    for i in excursions:
        for j in reg_excursions:
            if (i.id == j.reg_excursion_id) and (name.id == j.reg_user_id):
                excursion.append(i)
                reg_excursion.append(j)

    if (len(article) == 0) and (len(excursion) == 0):
        context = {
            'empty':'empty'
        }
    else:
        context = {
            'articles':article,
            'excursions':excursion,
            'reg_excursions':reg_excursion
        }
    
    return context

def cabinet(request):
    articles = Articles.objects.all()
    excursion = Excursions.objects.all()
    reg_excursion = Reg_Excursion.objects.all()
    name = request.user

    return render(request, 'profiles/cabinet.html', render_cabinet(name, articles, excursion, reg_excursion))

# Отображение странци по созданию статей и всех последующих манипуляция с данными и сохранениями их
def create_article(request):
    if request.method == "POST" and request.FILES:
        article_author = request.user.username
        article_caption = request.POST.get('name_article')
        article_discription = request.POST.get('mini_name')
        article_text = request.POST.get('articles_text')
        article_rank = request.POST.get('radioB')
        articles_image = request.FILES['article_image']

        article = Articles.objects.create(author = article_author, caption_name = article_caption, 
                                        caption_mini_text = article_discription, articles_text = article_text, 
                                        article_image = articles_image, ranks = article_rank)
        article.save()

        context = {
            'success':'Статья опубликована'
        }
        return render(request, 'profiles/create_article.html', context)

    return render(request, 'profiles/create_article.html')