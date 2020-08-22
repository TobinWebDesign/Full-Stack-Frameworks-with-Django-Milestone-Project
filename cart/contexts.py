from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from retreats.models import Retreat
from classes.models import Class

def cart_contents(request):

    """
    Makes the cart contents are available when rendering every page
    """

    cart_items = []
    total = 0
    product_count = 0
    cart = request.session.get('cart', {})

    for item_id, quantity in cart.items():
        try:
            product = Retreat.objects.get(sku=item_id)
        except Retreat.DoesNotExist:
            product = get_object_or_404(Class, sku=item_id)
        total += quantity * product.price
        product_count += quantity
        cart_items.append({            
            'item_id': item_id,
            'quantity': quantity,
            'retreat': product,
        })
    
    grand_total = total

    context = {
        'cart_items': cart_items,
        'total': total,
        'retreat_count': product_count,
        'grand_total': grand_total,
    }
    print(cart_items)
    print(grand_total)
    return context