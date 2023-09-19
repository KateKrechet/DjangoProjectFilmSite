from django.shortcuts import render
from django.http import HttpResponsePermanentRedirect


# Create your views here.
# def index(request):
#     return HttpResponsePermanentRedirect('/home')

def home(request):
    return render(request, 'index.html')


def persona(request, id):
    id = int(id)
    hero = ['Родион Меглин', 'Есения Стеклова', 'Женя', 'Александр Тихонов', 'Стеклов']
    who = ['Первоклассный детектив с психическим расстройством', 'Стажерка Меглина', 'Влюбленный одногруппник Есении',
           'Влюбленный одногруппник Есении', 'Отец Есении']
    actor = ['Константин Хабенский', 'Паулина Андреева', 'Александр Петров', 'Макар Запорожский', 'Виталий Кищенко']
    photo = ['img/8.jpg', 'img/9.jpg', 'img/10.jpg', 'img/11.jpg', 'img/12.jpg']
    hrefs = [
        'https://ru.wikipedia.org/wiki/%D0%A5%D0%B0%D0%B1%D0%B5%D0%BD%D1%81%D0%BA%D0%B8%D0%B9,_%D0%9A%D0%BE%D0%BD%D1%81%D1%82%D0%B0%D0%BD%D1%82%D0%B8%D0%BD_%D0%AE%D1%80%D1%8C%D0%B5%D0%B2%D0%B8%D1%87',
        'https://ru.wikipedia.org/wiki/%D0%90%D0%BD%D0%B4%D1%80%D0%B5%D0%B5%D0%B2%D0%B0,_%D0%9F%D0%B0%D1%83%D0%BB%D0%B8%D0%BD%D0%B0_%D0%9E%D0%BB%D0%B5%D0%B3%D0%BE%D0%B2%D0%BD%D0%B0',
        'https://ru.wikipedia.org/wiki/%D0%9F%D0%B5%D1%82%D1%80%D0%BE%D0%B2,_%D0%90%D0%BB%D0%B5%D0%BA%D1%81%D0%B0%D0%BD%D0%B4%D1%80_%D0%90%D0%BD%D0%B4%D1%80%D0%B5%D0%B5%D0%B2%D0%B8%D1%87_(%D0%B0%D0%BA%D1%82%D1%91%D1%80)',
        'https://24smi.org/celebrity/1043-makar-zaporozhskij.html',
        'https://ru.wikipedia.org/wiki/%D0%9A%D0%B8%D1%89%D0%B5%D0%BD%D0%BA%D0%BE,_%D0%92%D0%B8%D1%82%D0%B0%D0%BB%D0%B8%D0%B9_%D0%AD%D0%B4%D1%83%D0%B0%D1%80%D0%B4%D0%BE%D0%B2%D0%B8%D1%87']
    data = {'k1': actor[id], 'k2': hero[id], 'k3': who[id], 'k4': hrefs[id], 'k5': photo[id]}
    return render(request, 'persona.html', context=data)
