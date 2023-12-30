from django.contrib import admin
from django.urls import path
from .views.home import Home
from .views.signup import SignUp
from .views.login import Login, logout
from .views.cart import Cart
from .views.checkout import CheckOut
from .views.myorders import MyOrders
from store.middlewares.auth import auth_middleware, del_middleware


urlpatterns = [
    path('', Home.as_view()),
    path('signup/', SignUp.as_view()),
    path('login/', Login.as_view(),name='login'), 
    path('logout/', logout), 
    path('cart/', auth_middleware(Cart.as_view())), 
    path('check-out/', CheckOut.as_view()), 
    path('my-orders/', MyOrders.as_view()),
    path('cart/<id>', Cart.as_view()), 
]