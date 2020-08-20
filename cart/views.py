from django.shortcuts import render, redirect, reverse, HttpResponse, get_object_or_404
from django.contrib import messages

from retreats.models import Retreat
from classes.models import Class

# Create your views here.

def view_cart(request):
    """ A view that renders the shopping cart page """

    return render(request, 'cart/cart.html')

def add_to_cart(request, item_id):
    """ Add a quantity of the specified retreat to the shopping cart """

    retreat = get_object_or_404(Retreat, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    cart = request.session.get('cart', {})

    if item_id in list(cart.keys()):
        cart[item_id] += quantity
        messages.success(request, f'Updated {retreat.name} quantity to {cart[item_id]}'),
    else:
        cart[item_id] = quantity
        messages.success(request, f'Added {retreat.name} to your cart'),

    request.session['cart'] = cart
    return redirect(redirect_url)

def add_class_to_cart(request, item_id):
    """ Add a quantity of the specified yoga class to the shopping cart """

    class_detail = get_object_or_404(Class, sku=item_id)
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    cart = request.session.get('cart', {})

    if item_id in list(cart.keys()):
        cart[item_id] += quantity
        messages.success(request, f'Updated {class_detail.name} quantity to {cart[item_id]}')
    else:
        cart[item_id] = quantity
        messages.success(request, f'Added {class_detail.name} to your cart')

    request.session['cart'] = cart
    return redirect(redirect_url)

def adjust_cart(request, item_id):
    """ Adjust a quantity of the specified retreat to the shopping cart """

    retreat = get_object_or_404(Retreat, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    cart = request.session.get('cart', {})

    if quantity > 0:
        cart[item_id] = quantity
        messages.success(request, f'Updated {retreat.name} quantity to {cart[item_id]}')
    else:
        cart.pop(item_id)
        messages.success(request, f'Removed {retreat.name} from your cart')

    request.session['cart'] = cart
   
    return redirect(reverse('view_cart'))


def remove_from_cart(request, item_id):
    """ Remove a specified retreat to the shopping cart """
    retreat = get_object_or_404(Retreat, pk=item_id)
    cart = request.session.get('cart', {})
    
    cart.pop(item_id)
    messages.success(request, f'Removed {retreat.name} from your cart')
    request.session['cart'] = cart
   
    return HttpResponse(status=200)