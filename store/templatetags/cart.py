from django import template

register = template.Library()


@register.filter(name='cart_quantity')
def cart_quantity(product, cart):
    keys = cart.keys()
    for id in keys:
        if int(id) == product.id:
            return cart.get(id)


@register.filter(name='cart_total_price')
def cart_total_price(product, cart):
    keys = cart.keys()
    for id in keys:
        if int(id) == product.id:
            return product.price * cart_quantity(product, cart)


@register.filter(name='cart_total_cart_price')
def cart_total_cart_price(products, cart):
    sum = 0
    for p in products:
        sum += cart_total_price(p, cart)
    return sum
