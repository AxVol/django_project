from django.shortcuts import render, redirect
from django.utils import timezone

from .models import Articles, Comments
from homepage.views import searching

# Отображение главной страницы со всеми статьями
def articles(request):
    index_articles = Articles.objects.all()
    context = {
        'index_articles':index_articles
    }

    if request.method == "GET":
        if request.GET.get('Blog'):
            return render(request, 'articles/articles.html', searching(request.GET.get('Blog'), index_articles))
        elif request.GET.get('History'):
            return render(request, 'articles/articles.html', searching(request.GET.get('History'), index_articles))
        elif request.GET.get('Facts'):
            return render(request, 'articles/articles.html', searching(request.GET.get('Facts'), index_articles))
        elif request.GET.get('Guide'):
            return render(request, 'articles/articles.html', searching(request.GET.get('Guide'), index_articles))

    return render(request, 'articles/articles.html', context)

# Наполнение контентом страницы, подхдящий для запрошенной статьи на основе айди
def content(detail_articles, detail_comments, articles_id):
    for article in detail_articles:
        if article.id == articles_id:
              context = {
                'caption_name':article.caption_name,
                'articles_text':article.articles_text,
                'counter':article.count_comm,
                'image':article.article_image,
                'detail_comments':detail_comments,
                'articles_id':articles_id
            }
        
    return context

# Обработка конкретно полученной статьи на основе её айдишника
def article_detail(request, articles_id):
    detail_articles = Articles.objects.all()
    detail_comments = Comments.objects.all()

    try:
        if request.method == 'GET':  
            if request.GET.get('search'):
                return redirect(request, 'articles/articles.html', searching(request.GET.get('search'), detail_articles))

        if request.method == 'POST':
            comments = request.POST.get('comment')
            author_comm = request.user

            comm = Comments.objects.create(author = author_comm, comment_text = comments, pub_date = timezone.now(), 
                                          articles_id = articles_id)
            count = Articles.objects.get(pk = articles_id)
            count.count_comm += 1
            
            count.save()
            comm.save()
            
            return render(request, 'articles/article1.html', content(detail_articles, detail_comments, articles_id)) 
    except:   
        return render(request, 'articles/article1.html', content(detail_articles, detail_comments, articles_id))
    finally:
        return render(request, 'articles/article1.html', content(detail_articles, detail_comments, articles_id))