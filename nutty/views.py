from django.shortcuts import render,redirect
from django.db.models import F
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



def create_Basket(req, id):
    menu = Menu.objects.get(pk=id)
    user = req.user
    basket, _ = Basket.objects.get_or_create(user=user)

    # หา BasketItem ที่มี menu และ basket เหมือนกับที่เราต้องการสร้าง
    basket_item, created = BasketItem.objects.get_or_create(basket=basket, menu=menu)

    # ถ้า BasketItem มีอยู่แล้ว ให้เพิ่ม quantity ขึ้น 1
    if not created:
        basket_item.quantity = F('quantity') + 1
        basket_item.save()

    return redirect('read_Basket')

def poss(req, id):
    basket = BasketItem.objects.get(id=id)
    basket.quantity += 1
    basket.save()
    return redirect('read_Basket')


def nega(req, id):
    basket = BasketItem.objects.get(id=id)
    basket.quantity -= 1
    basket.save()
    return redirect('read_Basket')


def confirm(req):
    if req.method == 'POST':
        seat = req.POST.get('seat')
        more = req.POST.get('more')

        maps = f'{seat},{more}'

        seat = int(seat) if seat else None
        more = str(more) if more else None

        basket = Basket.objects.filter(user=req.user).first()

        # menu_items = [item.menu.name for item in basket.get_basket_items_list.all()]
        # menu_items_str = ', '.join(menu_items)

        # order = Order.objects.create(
        #     user=req.user,
        #     basket=basket,
        #     menu_item=menu_items_str,
        #     total_price=basket.get_basket_total,
        #     quantity=basket.get_basket_items,
        #     table_number=seat,
        #     note=more
        # )

        # Create Order for each item in the basket
        for item in basket.get_basket_items_list.all():
            Order.objects.create(
                user=req.user,
                basket=basket,
                menu_item=item.menu.name,
                total_price=item.get_total,
                quantity=item.quantity,
                table_number=seat,
                note=more
            )

        return redirect('index')


