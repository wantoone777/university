from datetime import datetime
import json
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.http import HttpResponse, HttpResponseNotFound, Http404
from .models import *


def track_visit(func):
    def wrapper(*args, **kwargs):
        func_dictionary = {"index": "I am from index", "all_unvs": "I am from all_unvs", "somepages": "I am from somepages", "after": "I am from after", "certain": "I am from certain", "to_universitygo": "I am from to_universytogo"}
        date = datetime.now()
        file = open('tracks.txt', 'r', encoding='utf-8')
        data = json.load(file)
        file.close()
        data[str(date)] = f'Step from {func_dictionary[func.__name__]}'
        
        file = open('tracks.txt', 'w', encoding='utf-8')
        json.dump(data, file, indent=4)
        
        r = func(*args, **kwargs)  # origin func
        
        return r
    
    return wrapper


@track_visit
def index(request):
    data = {}

    return render(request, 'universitygo/ru/index.html')


@track_visit
def all_unvs(request):
    data = {
        'title': 'Все учебные заведения',
        'unvs': University.objects.filter(is_published=True)
    }

    return render(request, 'universitygo/ru/all.html', context=data)


@track_visit
def somepages(request, unv_int):
    data = {'title': 'Страницы по int - {0}'.format(unv_int)}
    data['unvs'] = University.objects.filter(after=unv_int, is_published=True)

    return render(request, "universitygo/ru/all.html", context=data)


@track_visit
def after(request, after_id):
    if after_id == '9':
        data = {
            'title': 'Заведения после 9 класса',
            'unvs': University.objects.filter(is_after9=True)
        }
    else:
        data = {
            'title': 'Заведения после 11 класса',
            'unvs': University.objects.filter(is_after11=True)
        }
    
    return render(request, context=data)


@track_visit
def certain(request, unv_id):
    unv = University.objects.get(pk=unv_id)
    data = {
        'title': 'Учебное заведение по id - {0}'.format(unv_id),
        'unv': unv,
    }

    return render(request, "universitygo/ru/certain.html", context=data)


@track_visit
def to_universitygo(request):
    return redirect('/universitygo/', permanent=False)
