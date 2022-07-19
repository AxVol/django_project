from django.contrib import admin

from .models import Excursions

class ExcursionAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Excursion information', {'fields' : ['caption_name']}),
        (None, {'fields': ['caption_mini_text']}),
        (None, {'fields' : ['price']}),
        (None, {'fields' : ['place']}),
        ('Date information', {'fields' : ['duraction_in_hour']}),
        (None, {'fields' : ['date_ex']}),
        (None, {'fields' : ['time_ex']}),
        ('Rank excursion', {'fields' : ['ranks']}),
        ('Image information', {'fields' : ['excursion_image']})
    ]

    list_display = ('caption_name', 'price', 'place')
    list_filter = ['duraction_in_hour']
    search_fields = ['caption_name']

admin.site.register(Excursions, ExcursionAdmin)