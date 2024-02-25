from django.urls import path
from .views import *

urlpatterns = [
    path('',index,name='index'),
    path('read_Basket/',read_Basket,name='read_Basket'),
    path('create_Basket/<int:id>/',create_Basket,name='create_Basket'),
    path('poss/<int:id>/',poss,name='poss'),
    path('nega/<int:id>/',nega,name='nega'),
    path('confirm/',confirm,name='confirm'),




    
]