from django.shortcuts import render, redirect,get_object_or_404
from django.core.exceptions import ObjectDoesNotExist
from . models import *
from shop.models import *

# Create your views here.
def cart_details(request, tot=0, count=0, ct_iems=None):
    try:
        ct=cartlist.objects.get(cart_id=c_id(request))
        ct_items=Items.objects.filter(cart=ct,active=True)
        for i in ct_items:
            tot +=(i.prodt.P_price*i.quantity)
            count += i.quantity
    except ObjectDoesNotExist:
        pass


    return render(request,'cart.html',{'ci':ct_items,'cn':count,'t':tot})
def c_id(request):
    ct_id=request.session.session_key
    if not ct_id:
        ct_id=request.session.create()
    return ct_id
def add_cart(request,product_id):
    prod=Product.objects.get(id=product_id)
    try:
        ct=cartlist.objects.get(cart_id=c_id(request))
    except cartlist.DoesNotExist:
        ct=cartlist.objects.create(cart_id=c_id(request))
        ct.save()
    try:
        c_items=Items.objects.get(prodt=prod,cart=ct)
        if c_items.quantity < c_items.prodt.P_stock:
            c_items.quantity+=1
        c_items.save()

    except Items.DoesNotExist:
        c_items=Items.objects.create(prodt=prod,quantity=1,cart=ct)
        c_items.save()

    return redirect('cartDetails')


def min_cart(request,product_id):
    ct=cartlist.objects.get(cart_id=c_id(request))
    prod=get_object_or_404(Product,id=product_id)
    c_items=Items.objects.get(prodt=prod,cart=ct)
    if c_items.quantity>1:
        c_items.quantity=1
        c_items.save()
    else:
        c_items.delete()
    return redirect('cartDetails')



def cart_delete(request,product_id=0):
    ct = cartlist.objects.get(cart_id=c_id(request))
    prod = get_object_or_404(Product, id=product_id)
    c_items = Items.objects.get(prodt=prod, cart=ct)
    c_items.delete()
    return redirect('cartDetails')
