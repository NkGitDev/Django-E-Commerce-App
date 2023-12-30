from django.views import View
from django.shortcuts import render
from store.models.product import Product

class Cart(View):
    def get(self, request, id=None):
        ids = list(request.session.get('cart').keys())
        cart_products = Product.get_product_by_id(ids)
        # print(cart_products)

        # Note: this code is deleting main products
        # if id != None:
        #     cart_item = Product.objects.get(id=id)
        #     # print(cart_item)
        #     cart_item.delete()

        return render(request, 'cart.html', {'user_cart_prd':cart_products})
    
