from django.shortcuts import render, redirect, get_object_or_404
from store.models import Product

def _get_cart(request):
    return request.session.setdefault('cart', {})

def add_to_cart(request, product_id):
    cart = _get_cart(request)
    pid = str(product_id)
    cart[pid] = cart.get(pid, 0) + 1
    request.session.modified = True
    return redirect('cart:view')

def view_cart(request):
    cart = _get_cart(request)
    items = []
    total = 0
    for pid, qty in cart.items():
        prod = get_object_or_404(Product, pk=int(pid))
        subtotal = prod.price * qty
        items.append({'product': prod, 'qty': qty, 'subtotal': subtotal})
        total += subtotal
    return render(request, 'cart/cart.html', {'items': items, 'total': total})

def remove_item(request, product_id):
    cart = _get_cart(request)
    pid = str(product_id)
    if pid in cart:
        del cart[pid]
        request.session.modified = True
    return redirect('cart:view')
