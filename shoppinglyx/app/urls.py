from django.urls import path
from app import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    # path('', views.home),
    path('', views.ProductView.as_view(), name="home"),
    path('product-detail/<int:pk>', views.product_detail.as_view(), name='product-detail'),
    path('cart/', views.add_to_cart, name='add-to-cart'),
    path('buy/', views.buy_now, name='buy-now'),
    path('profile/', views.profile, name='profile'),
    path('address/', views.address, name='address'),
    path('orders/', views.orders, name='orders'),
    path('changepassword/', views.change_password, name='changepassword'),
    path('mobile/', views.mobile, name='mobile'),
    path('mobile/<slug:data>', views.mobile, name='mobiledata'),
    path('login/', views.login, name='login'),
    path('registration/', views.customerregistration, name='customerregistration'),
    path('checkout/', views.checkout, name='checkout'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



# By chatgpt ------------------->
# from django.urls import path
# from app import views
# from django.conf import settings
# from django.conf.urls.static import static

# urlpatterns = [
#     path('', views.home),
#     path('product-detail/', views.product_detail, name='product-detail'),
#     path('cart/', views.add_to_cart, name='add-to-cart'),
#     path('buy/', views.buy_now, name='buy-now'),
#     path('profile/', views.profile, name='profile'),
#     path('address/', views.address, name='address'),
#     path('orders/', views.orders, name='orders'),
#     path('changepassword/', views.change_password, name='changepassword'),
#     path('mobile/', views.mobile, name='mobile'),
#     path('login/', views.login, name='login'),
#     path('registration/', views.customerregistration, name='customerregistration'),
#     path('checkout/', views.checkout, name='checkout'),
# ]

# if settings.DEBUG:  # Serve media files only in development mode
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
