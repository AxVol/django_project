from django.contrib import admin
from .models import Articles, Comments

class CommentsInLine(admin.TabularInline):
    model = Comments

class ArticlesAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Author Article', {'fields': ['author']}),
        ('Article information', {'fields' : ['caption_name']}),
        (None, {'fields': ['caption_mini_text']}),
        (None, {'fields' : ['articles_text']}),
        ('Rank article', {'fields' : ['ranks']}),
        ('Date information', {'fields' : ['pub_date']}),
        ('Image information', {'fields' : ['article_image']})
    ]
    inlines = [CommentsInLine]

    list_display = ('caption_name', 'pub_date', 'ranks')
    list_filter = ['pub_date']
    search_fields = ['caption_name']

admin.site.register(Articles, ArticlesAdmin)