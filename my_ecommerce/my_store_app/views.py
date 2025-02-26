from django.shortcuts import render
from .models import *
from django.http import JsonResponse
import json
import datetime
from . utils import cookieCart, cartData, guestOrder
# Create your views here.


def store(request):
    data = cartData(request)
    cartItems = data['cartItems']
    order = data['order']
    items = data['items']

    products = Product.objects.all()
    context = {'products':products, "cartItems":cartItems, 'shipping':False}
    return render(request, 'my_store_app/store.html', context)

def checkout(request):
    data = cartData(request)
    cartItems = data['cartItems']
    order = data['order']
    items = data['items']

    context = {'items':items, 'order':order, "cartItems":cartItems, 'shipping':False}
    return render(request, 'my_store_app/checkout.html', context)

def cart(request):

    data = cartData(request)
    cartItems = data['cartItems']
    order = data['order']
    items = data['items']

    context = {'items':items, 'order':order, "cartItems":cartItems, 'shipping':False}
    return render(request, 'my_store_app/cart.html', context)


def updateItem(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']
    # print('productId:', productId)
    # print('action:', action)

    customer = request.user.customer
    product = Product.objects.get(id=productId)
    order, created = Order.objects.get_or_create(customer=customer, complete=False)
    orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)

    if action == "add":
        orderItem.quantity = (orderItem.quantity + 1)
    elif action == "remove":
        orderItem.quantity = (orderItem.quantity - 1)

    orderItem.save()

    if orderItem.quantity <= 0:
        orderItem.delete()

    return JsonResponse("item was added", safe=False)


def processOrder(request):
	transaction_id = datetime.datetime.now().timestamp()
	data = json.loads(request.body)

	if request.user.is_authenticated:
		customer = request.user.customer
		order, created = Order.objects.get_or_create(customer=customer, complete=False)

	else:
		customer, order = guestOrder(request, data)

		# for item in items:
		# 	product = Product.objects.get(id=item['id'])
		# 	orderItem = OrderItem.objects.create(
		# 		product=product,
		# 		order=order,
		# 		quantity=item['quantity'],
		# 	)

	total = float(data['form']['total'])
	order.transaction_id = transaction_id

	if total == order.get_cart_total:
		order.complete = True
	order.save()

	if order.shipping == True:
		ShippingAddress.objects.create(
		customer=customer,
		order=order,
		address=data['shipping']['address'],
		city=data['shipping']['city'],
		state=data['shipping']['state'],
		zipcode=data['shipping']['zipcode'],
		)

	return JsonResponse('Payment submitted..', safe=False)


def product_detail(request, id):
    product = Product.objects.get(id=id)  # Fetch the product by its ID
    all_products = Product.objects.all()
    context = {'product': product, 'allproducts':all_products}
    return render(request, 'my_store_app/sproduct.html', context)

def blog(request):
    # context = {}
    return render(request, 'my_store_app/blog.html')

def contact(request):
    # context = {}
    return render(request, 'my_store_app/contact.html')

def about(request):
    # context = {}
    return render(request, 'my_store_app/about.html')

