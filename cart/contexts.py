from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from retreats.models import Retreat

def cart_contents(request):

    """
    Makes the cart contents are available when rendering every page
    """

    cart_items = []
    total = 0
    retreat_count = 0
    cart = request.session.get('cart', {})

    for item_id, quantity in cart.items():
        retreat = get_object_or_404(Retreat, pk=item_id)
        total += quantity * retreat.price
        retreat_count += quantity
        cart_items.append({
            'item_id': item_id,
            'quantity': quantity,
            'retreat': retreat,
        })
    
    grand_total = total

    context = {
        'cart_items': cart_items,
        'total': total,
        'retreat_count': retreat_count,
        'grand_total': grand_total,
    }

    return context