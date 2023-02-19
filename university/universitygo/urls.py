from django.urls import path

from .views import *


urlpatterns = [
    path('', index, name='index'),
    path('all/', all_unvs, name='all_unvs'),
    path('somepages/<int:unv_int>/', somepages, name='somepages'),
    path('after/<int:after_id>/', after, name='after'),
    path('university/<int:unv_id>/', certain, name='certain'),
]