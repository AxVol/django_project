from django.shortcuts import render

from .models import Excursions, Reg_Excursion
from homepage.views import searching

# Отображение главной страницы со всеми экскурсиями
def excursion_view(request):
    index_excursion = Excursions.objects.all()
    context = {
        'index_excursion':index_excursion
    }

    if request.method == "GET":
        if request.GET.get('Streets'):
            return render(request, 'excursion/excursions.html', searching(request.GET.get('Streets'), index_excursion))
        elif request.GET.get('Historical'):
            return render(request, 'excursion/excursions.html', searching(request.GET.get('Historical'), index_excursion))
        elif request.GET.get('Buildings'):
            return render(request, 'excursion/excursions.html', searching(request.GET.get('Buildings'), index_excursion))

    return render(request, 'excursion/excursions.html', context)

# Наполнение контентом страниц
def content(detail_excursion, excursion_id):
    for excursion in detail_excursion:
        if excursion.id == excursion_id:
            time = excursion.time_ex.split(',')
            date = excursion.date_ex.split(',')
            
            context = {
                'id':excursion_id,
                'caption_name':excursion.caption_name,
                'caption_mini_text':excursion.caption_mini_text,
                'duraction_in_hour':excursion.duraction_in_hour,
                'date_ex':date,
                'time_ex':time,
                'price':excursion.price,
                'place':excursion.place,
                'register':excursion.registred,
                'excursion_image':excursion.excursion_image,
            }
        
    return context

# Отображение конкретно выбранной статьи на основе её айди
def excursion_detail(request, excursion_id):
    detail_excursion = Excursions.objects.all()  

    return render(request, 'excursion/excursion1.html', content(detail_excursion, excursion_id))

# Страница с регистрацией на экскурсию
def register_excursion(request, excursion_id):
    detail_excursion = Excursions.objects.all()

    if request.method == "POST":
        reg_user = request.user.id
        ex_id = excursion_id
        register_people = int(request.POST.get("count_people"))
        date = request.POST.get("date")
        
        # Махинации и крутилки с проверками, чтобы на экскурсию не могло записаться сверх максимального количества людей
        # В обратном случае, все хорошо и запись проходит
        excursion = Excursions.objects.get(pk = ex_id)
        reg = excursion.registred
        excursion.registred += register_people
        
        if excursion.registred >= excursion.place:
            difference = excursion.place - reg
            
            context = {
                'overflowing':'overflowing',
                'difference':difference,
            }
            return render(request, 'excursion/register_ex.html', context)
        else:
            ex_reg = Reg_Excursion.objects.create(reg_user_id = reg_user, reg_excursion_id = ex_id, 
                                                reg_date = date, reg_people = register_people)
            excursion.save()
            ex_reg.save()

            context = {
                'succes':'succes'
            }
            return render(request, 'excursion/register_ex.html', context)

    return render(request, 'excursion/register_ex.html', content(detail_excursion, excursion_id))