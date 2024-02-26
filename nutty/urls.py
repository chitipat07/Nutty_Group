from django.urls import path
from .views import *

urlpatterns = [
    path('',index,name='index'),
    path('read_Basket/',read_Basket,name='read_Basket'),
    path('create_Basket/<int:id>/',create_Basket,name='create_Basket'),
    path('poss/<int:id>/',poss,name='poss'),
    path('nega/<int:id>/',nega,name='nega'),
    path('confirm/',confirm,name='confirm'),
    path('read_for_admin/',read_for_admin,name='read_for_admin'),
    path('read_for_user/',read_for_user,name='read_for_user'),
    path('create_menu/',create_menu,name='create_menu'),
    path('update_menu/<int:id>/',update_menu,name='update_menu'),
    path('delete/<int:id>/',delete,name='delete'),
    path('delete_item/<int:id>/',Delete_item,name='delete_item'),
    path('register_user/',register_user,name='register_user'),
    path('logins_user/',logins_user,name='logins_user'),
    path('logout_view/',logout_view,name='logout_view'),
    path('success_page/',success_page,name='success_page'),

    # path('show_order_summary/',show_order_summary,name='show_order_summary'),


]