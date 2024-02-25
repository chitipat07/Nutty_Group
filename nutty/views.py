from django.shortcuts import render,redirect
from django.db.models import F
from .models import *
from .forms import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test

def is_active_and_not_superuser(user):
    return user.is_active and not user.is_superuser

def is_manager(user):
    return user.is_superuser and user.is_staff
# Create your views here.
def index(req):
    return render(req,'nutty/index.html')

def register_user(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('logins_user') 
    else:
        form = UserCreationForm()

    return render(request, 'nutty/register.html', {'form': form})


def logins_user(req):
    form = Loginforms()
    if req.method == 'POST':
        form = Loginforms(req.POST)
        if form.is_valid:
            username = req.POST.get('username')
            password = req.POST.get('password')
            users = authenticate(username=username,password=password)
            if users:
                login(req,users)
                return redirect('read_for_user')
        else:
            form = Loginforms()
    return render(req, 'nutty/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('index')

########################################################################################
# for user
@login_required(login_url='logout_view')
@user_passes_test(is_active_and_not_superuser, login_url='/read_for_admin')
def read_for_user(req):
    data = Menu.objects.all()
    context = {
        'data':data
    }
    return render(req,'nutty/read_foruser.html',context)

########################################################################################
# for admin
@login_required(login_url='logout_view')
@user_passes_test(is_manager, login_url='logout_view')
def read_for_admin(req):
    data = Menu.objects.all()
    context = {
        'data':data
    }
    return render(req,'nutty/read_foradmin.html',context)

def create_menu(req):
    form = MenuForm()
    if req.method == 'POST':
        form = MenuForm(req.POST,req.FILES)
        if form.is_valid():
            form.save()
            return redirect('read_for_admin')
        else:
            form = MenuForm()
    return render(req,'nutty/create.html',{'form':form})

def update_menu(req,id):
    data = Menu.objects.get(pk=id)
    form = MenuForm(instance=data)
    if req.method == 'POST':
        form = MenuForm(req.POST,req.FILES,instance=data)
        if form.is_valid():
            form.save()
            return redirect('read_for_admin')
        else:
            form = MenuForm(instance=data)
    return render(req,'nutty/update.html',{'form':form,'data':data})

def delete(req,id):
    data = Menu.objects.get(pk=id)
    data.delete()
    return redirect('read_for_admin')

########################################################################################
# add basket
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

def Delete_item(req,id):
    data = BasketItem.objects.get(pk=id)
    data.delete()
    return redirect('read_Basket')
