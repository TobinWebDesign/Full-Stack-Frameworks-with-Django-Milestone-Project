from django.shortcuts import render, redirect, reverse, HttpResponse, get_object_or_404
from django.contrib import messages

from retreats.models import Retreat
from classes.models import Class

# Create your views here.

def view_cart(request):
    """ A view that renders the shopping cart page """

    return render(request, 'cart/cart.html')

def add_to_cart(request, item_id, type):
    """ Add a quantity of the specified retreats to the shopping cart """
    # create a model to include both Class and Retreat
    product_models = {
        "class": Class,
        "retreat": Retreat,
    }

    model = product_models.get(type)
    product = get_object_or_404(model, pk=item_id)
    # to split the Class and Retreat types
    product_type_id = type+'_'+str(item_id)

    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    cart = request.session.get('cart', {})
    
    if product_type_id in list(cart.keys()):
        cart[product_type_id] += quantity
        messages.success(request, f'Updated {product.name} quantity to {cart[product_type_id]}'),
    else:
        cart[product_type_id] = quantity
        messages.success(request, f'Added {product.name} to your cart'),

    request.session['cart'] = cart
    return redirect(redirect_url)


def adjust_cart(request, item):
    """ Adjust a quantity of the specified retreat and class to the shopping cart """
    
    # item is either Class+pk or Retreat+id
    #product = item
    quantity = int(request.POST.get('quantity'))
    cart = request.session.get('cart', {})

    if quantity > 0:
        cart[item] = quantity
        messages.success(request, f'Your cart has been Updated')
    else:
        cart.pop(item)
        messages.success(request, f'Item has been removed Removed')

    request.session['cart'] = cart
   
    return redirect(reverse('view_cart'))


def remove_from_cart(request, item):
    """ Remove a specified retreat to the shopping cart """     
    cart = request.session.get('cart', {})
    
    cart.pop(item)
    messages.success(request, f'Item has been removed Removed')
    request.session['cart'] = cart
   
    return HttpResponse(status=200)