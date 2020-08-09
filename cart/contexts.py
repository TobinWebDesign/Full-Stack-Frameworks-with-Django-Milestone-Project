from decimal import Decimal
from django.conf import settings

def cart_contents(request):

    """
    Makes the cart contents are available when rendering every page
    """

    cart_items = []
    total = 0
    retreat_count = 0

    context = {
        'cart_items': cart_items,
        'total': total,
        'retreat_count': retreat_count,
    }

    return context