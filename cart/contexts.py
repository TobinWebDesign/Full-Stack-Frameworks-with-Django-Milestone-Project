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
    print(cart)

    for item_id, quantity in cart.items():
        item_type_and_id = item_id.split('_')
        product_type=item_type_and_id[0]
        product_id=item_type_and_id[1]
        if(product_type=='retreat'):
            try:
                product = Retreat.objects.get(pk=product_id)
            except Retreat.DoesNotExist:
                #product = get_object_or_404(Class, pk=item_id)
                print("Product does not exist")
        else:# Type is Class here
            try:
                product = Class.objects.get(pk=product_id)
            except Class.DoesNotExist:
                #product = get_object_or_404(Class, pk=item_id)
                print("Class does not exist")

        total += quantity * product.price
        product_count += quantity
        cart_items.append({
            'item_id': product_id,
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