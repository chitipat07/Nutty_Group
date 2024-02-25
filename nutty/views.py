from django.shortcuts import render,redirect
from .models import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test

# Create your views here.
def index(req):
    item = Menu.objects.all()
    context = {
        'data':item
    }
    return render(req,'nutty/read_foruser.html',context)


# def create_Basket(req,id):
#     fs = BeamChi.objects.get(pk=id)

#     existing_basket = Basket.objects.filter(user=req.user, menu_item=fs).first()

#     if existing_basket:
 
#         existing_basket.q += 1
#         existing_basket.save()
#     else:

#         B = Basket.objects.create(user=req.user, menu_item=fs, total_price=fs.g)
#         B.save()
#     return redirect('read_basket')



def read_Basket(req):
    if req.user.is_authenticated:
        basket, created = Basket.objects.get_or_create(user=req.user)
        item = basket.basketitem_set.all()
    else:
        item = []
        basket = {'get_basket_total':0,'get_basket_items':0}
    context = {
        'data':item,
        'basket':basket
    }
    return render(req,'nutty/basket.html', context)



# def create_Basket(req,id):
#     menu = Menu.objects.get(pk=id)
#     user = req.user
#     basket,_ = Basket.objects.get_or_create(user=user)

#     basket_item = BasketItem.objects.create(basket=basket,menu=menu)

#     return redirect('read_Basket')