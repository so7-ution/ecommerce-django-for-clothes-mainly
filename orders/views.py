from django.shortcuts import render, redirect
from carts.models import CartItem
from django.http import HttpResponse
from .forms import OrderForm
import datetime
from .models import Order
# Create your views here.
def place_order(request, total = 0, quantity = 0,):
    current_user = request.user

    cart_items = CartItem.objects
    cart_count = cart_items.count()
    if cart_count <= 0:
        return redirect('home')

    grand_total = 0

    #for cart_item in cart_items:
        #total += (cart_item.product.price * cart_item.quantity)
        #quantity += cart_item.quantity
    #grand_total = total

    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            data = Order()
            data.name = form.cleaned_data['name']
            data.phone = form.cleaned_data['phone']
            data.subcity = form.cleaned_data['subcity']
            data.detail_Address = form.cleaned_data['detail_Address']
            data.order_note = form.cleaned_data['order_note']
            data.order_total = grand_total
            data.ip = request.META.get("REMOTE_ADDR")
            data.save()

            yr= int (datetime.date.today().strftime('%Y'))
            dt= int (datetime.date.today().strftime('%d'))
            mt= int (datetime.date.today().strftime('%m'))
            d = datetime.date(yr, mt, dt)
            current_date = d.strftime("%Y%m%d")
            order_number = current_date + str(data.id)
            data.order_number = order_number
            data.save()
            return redirect('checkout')
    else:
        return redirect('checkout')
