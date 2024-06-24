from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('aboutUs', views.aboutUs, name='aboutUs'),
    path('photoGallery', views.photoGallery, name='photoGallery'),
    path('contact', views.contact, name='contact'),
    path('login', views.login, name='login'),
    path('registrar', views.registrar, name='registrar'),
    path('cart', views.cart, name='cart'),
    path('freeEat', views.freeEat, name='freeEat'),
    path('management', views.management, name='management'),
    path('profile/', views.profile, name='profile'),
    path('show_profile', views.show_profile, name='show_profile'),
    
    path('products', views.products, name='products'),
    path('product/manage', views.products_manage, name="product_manage"),
    path('product/add', views.product_add, name="product_add"),
    path('product/<id>/edit', views.product_edit, name="product_edit"),
    path('product/<id>/delete', views.product_delete, name="product_delete"),
    path('shopping-cart/add/<id>', views.shopping_cart_add, name="shopping_cart_add"),
    path('shopping-cart/substract/<id>', views.shopping_cart_substract, name="shopping_cart_substract"),
    path('shopping-cart/delete/<id>', views.shopping_cart_delete, name="shopping_cart_delete"),
    path('shopping-cart/clear', views.shopping_cart_clear, name="shopping_cart_clear"),
    path('shopping-cart/open', views.shopping_cart_open, name="shopping_cart_open"),
    path('shopping-cart/close', views.shopping_cart_close, name="shopping_cart_close"),
    path('create-order/', views.create_order, name='create_order'),
    path('orders/', views.orders, name='orders'),
]