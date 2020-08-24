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

    for item, quantity in cart.items():
        item_type_and_id = item.split('_') #Split the retreats and classes item into types and ids
        product_type=item_type_and_id[0]
        item_id=item_type_and_id[1]
        if(product_type=='retreat'):
            try:
                product = Retreat.objects.get(pk=item_id)
            except Retreat.DoesNotExist:                
                print("Product does not exist")
        else:# Type is Class here
            try:
                product = Class.objects.get(pk=item_id)
            except Class.DoesNotExist:                
                print("Class does not exist")

        total += quantity * product.price
        product_count += quantity
        cart_items.append({
            'item_id': item_id,
            'quantity': quantity,
            'product': product,
            'item': item,
        })
        print(item_type_and_id)
        print(item_id)
        print(item)
        
    grand_total = total

    context = {
        'cart_items': cart_items,
        'total': total,
        'retreat_count': product_count,
        'grand_total': grand_total,
    }
    
    return context