from django.shortcuts import render
from store.models import Product
from django.http import HttpResponse
# test için
from carts.models import Cart, CartItem
from carts.views import session


def home(request):
    products = Product.objects.all().filter(is_available=True)
    context = {
        'products': products,
    }
    return render(request, 'home.html', context)


def test(request):
    try:
        cart_id = session(request)
        print('cart_id : ' + cart_id)

    except:
        print('cart_id bulunamadı')

    try:
        cart = Cart.objects.get(cart_id=cart_id)
        print('cart : ' + str(cart))
    except:
        print('cart bulunamadı')
    try:
        is_cart_item_exists = CartItem.objects.filter(cart_id=cart.id).exists()
        print('cart var mı : '+ str(is_cart_item_exists))
    except:
        print('en sonu yok')






    print('cart :' +str(cart))


    # return HttpResponse('cart_id :' + cart_id + ' ' + 'cart: ' + str(cart))
