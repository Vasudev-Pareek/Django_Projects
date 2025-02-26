from django.urls import path
from .views import ProductListCreateView # for rest framework
from . import views

urlpatterns = [
    path('', views.Home, name="home"),
    path('about/', views.about, name='about'),
    path('cart/', views.cart, name='cart'),
    # path('news/', views.news, name='news'),
    path('checkout/', views.checkout, name='checkout'),
    path('contact/', views.contact, name='contact'),
    path('news/', views.news, name='news'),
    path('shop/', views.shop, name='shop'),
    path('singleNews/<int:id>/', views.singleNews, name='singleNews'),  
    path('singlePoduct/<int:id>/', views.singlePoduct, name='singlePoduct'),
    # path('AddCart/<int:id>/', views.AddCart, name='AddCart'),
    path('add-to-cart/', views.add_to_cart, name='add_to_cart'),
    path('signin/', views.signin, name='signin'),
    path('signup/', views.signup, name='signup'),
    path('signout/', views.signout, name='signout'),
    path('products/', ProductListCreateView.as_view(), name='product-list-create'), # for rest framework
]