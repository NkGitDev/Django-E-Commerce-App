from django.views import View
from django.shortcuts import redirect
from store.models import Product
from store.models import Orders
from store.models.customer import Customer

class CheckOut(View):
    def post(self, request):
        # print(request.POST)
        address = request.POST.get('inp_checkout_address')
        mobile = request.POST.get('inp_checkout_mobile')
        customer = request.session.get('customer_id')
        cart = request.session.get('cart')
        products = Product.get_product_by_id(list(cart.keys()))

        # print(address, mobile, customer, cart, products)

        for product in products:
            orders = Orders(
                order_product = product,
                order_customer = Customer(id = customer),
                order_qty = cart.get(str(product.id)),
                order_price = product.prod_price,
                order_address = address,
                order_mobile = mobile,
            )

            orders.save()
        request.session['cart'] = {}

        return redirect('/cart/')
    
