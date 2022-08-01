from rest_framework_nested import routers

from django.contrib import admin
from django.urls import path, include
from .views.home import Index , store
from .views.signup import Signup
from .views.login import Login , logout
from .views.cart import Cart
from .views.checkout import CheckOut
from .views.orders import OrderView
from store.views.api import ProductViewSet
from .middlewares.auth import  auth_middleware

from sites.urls import router as site_router


router = routers.NestedSimpleRouter(site_router, "domains", lookup="domain")
router.register("catalog", ProductViewSet)


urlpatterns = [
    path('index', Index.as_view(), name='homepage'),
    path('store', store, name='store'),
    path("", include(router.urls)),

    path('signup', Signup.as_view(), name='signup'),
    path('login', Login.as_view(), name='login'),
    path('logout', logout , name='logout'),
    path('cart', auth_middleware(Cart.as_view()) , name='cart'),
    path('check-out', CheckOut.as_view() , name='checkout'),
    path('orders', auth_middleware(OrderView.as_view()), name='orders'),

]
