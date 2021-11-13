from main.models import Cart


def set_cart_id_to_session(request, cart):
    request.session['cart_id'] = cart.id
    return {'items_in_cart': cart.items.count(), 'cart': cart}


def cart_processor(request):
    if 'cart_id' in request.session:
        cart = Cart.objects.get(id=request.session['cart_id'])
        return {'items_in_cart': cart.items.count(), 'cart': cart}

    elif request.user.is_authenticated:
        last_cart = request.user.cart_set.last()
        if not last_cart.completed:
            return set_cart_id_to_session(request, last_cart)

        else:
            cart = Cart.objects.create(user=request.user)
            return set_cart_id_to_session(request, cart)

    return {'items_in_cart': 0}
