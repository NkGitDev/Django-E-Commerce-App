from django.views import View
from django.shortcuts import render
from store.models import Orders

class MyOrders(View):

    def get(self, request):
        customer = request.session.get('customer_id')
        orders = Orders.get_orders_by_customer(customer)
        # print(orders)
        orders = reversed(orders)
        return render(request, 'orders.html', {'orders':orders})
        