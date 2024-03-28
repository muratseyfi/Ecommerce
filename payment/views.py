from django.shortcuts import render
from cart.cart import Cart
from payment.forms import ShippingForm
from payment.models import ShippingAddress


def checkout(request):
    # Get the cart
    cart = Cart(request)
    cart_products = cart.get_prods
    quantities = cart.cart_quants
    totals = cart.cart_total()

    if request.user.is_authenticated:
        # Checkout as logged in
        shipping_user = ShippingAddress.objects.get(user__id=request.user.id)
        shipping_form = ShippingForm(request.POST or None, instance=shipping_user)
        context = {
            'cart_products': cart_products, 
            'quantities': quantities, 
            'totals': totals,
            'shipping_form': shipping_form
            }
        
        return render(request, 'payment/checkout.html', context)
    else:
        # Checkout as guest
        shipping_form = ShippingForm(request.POST or None)
        context = {
            'cart_products': cart_products, 
            'quantities': quantities, 
            'totals': totals,
            'shipping_form': shipping_form
            }
        
        return render(request, 'payment/checkout.html', context)


def payment_success(request):
    return render(request, 'payment/payment_success.html', {})


