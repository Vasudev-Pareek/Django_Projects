from django.shortcuts import render, HttpResponse, redirect
from .models import *
from django.shortcuts import get_object_or_404
from .forms import CommentForm
from django.contrib import messages
from django.contrib.auth.models import User, auth
from django.contrib.auth import authenticate, logout
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.core.paginator import Paginator
from math import *
import json


def base(request):
    cart_items = Cart.objects.filter(user=request.user)
    cart_count = cart_items.count()
    return render(request, 'base.html', {'cart_count':cart_count})

def signin(request):
    if not request.user.is_authenticated and 'next' in request.GET:
        messages.info(request, "Please log in to continue to the requested page.")

    if request.method == "POST":
        uname = request.POST["useremail"]
        upassword = request.POST["Password"]

        user = authenticate(username = uname, password=upassword)
        
        if user is not None:
            auth.login(request, user)
            return redirect("/")
        else:
            messages.info(request, "invalid username or password")
            return redirect("signin")
        # return render(request, "index_2.html", {"user": request.user})
    else:
        return render(request, "signin.html", {"user": None})
    return render(request, 'signin.html')

def signup(request):
    if request.method == 'POST':
        fn = request.POST['firstname']
        lt = request.POST['lastname']
        em = request.POST['useremail']
        us = request.POST['username']
        psd1 = request.POST['Password']
        psd2 = request.POST['ConfirmPassword']

        if psd1 == psd2:
            if User.objects.filter(email=em).exists():
                messages.info(request, "Email is already used by another one")
                return render(request, "signup.html")
            elif User.objects.filter(username=us).exists():
                messages.info(request, "username is already used by another one")
                return render(request, "signup.html")
            else:
                user = User.objects.create_user(username=us, password=psd1, email=em, first_name=fn, last_name=lt)
                user.save()
            return redirect("signin")
        else:
            return redirect("signup")
    return render(request, 'signup.html')

def signout(request):
    logout(request)
    return redirect("/")

# Create your views here.
def Home(request):
    if request.user.is_authenticated:
        cart_items = Cart.objects.filter(user=request.user)
        cart_count = cart_items.count()
    else:
        # Logic for anonymous users
        cart_count = 0  # No items in cart for anonymous users

    # cart_items = Cart.objects.filter(user=request.user)
    # cart_count = cart_items.count()
    owners = shopowner.objects.all()
    companylogos = CompanyLogo.objects.all()
    df = products.objects.all()[:3]  # Get first 3 items
    news = productnews.objects.all()[:3]
    context = {
        'data':df, 
        'news':news, 
        'owners':owners, 
        'companylogos': companylogos,
        'cart_count':cart_count
    }
    return render(request, "index_2.html", context)

def about(request):
    if request.user.is_authenticated:
        cart_items = Cart.objects.filter(user=request.user)
        cart_count = cart_items.count()
    else:
        cart_items = []
        cart_count =0 

    owners = shopowner.objects.all()
    companylogos = CompanyLogo.objects.all()
    context = {
        'owners':owners, 
        'companylogos':companylogos, 
        'cart_count':cart_count
    }
    return render(request, "about.html", context)

def cart(request):
    if request.user.is_authenticated:
        cart_items = Cart.objects.filter(user=request.user)
        cart_count = cart_items.count()
    else:
        cart_count = 0
        cart_items = []

    grand_Total = sum(item.total_price for item in cart_items)
    companylogos = CompanyLogo.objects.all()
    context = {
        'cart_items': cart_items, 
        'companylogos':companylogos, 
        'cart_count':cart_count,
        'grand_Total':grand_Total,
    }
    return render(request, 'cart.html',context)

@login_required
def checkout(request):
    if request.user.is_authenticated:
        cart_items = Cart.objects.filter(user=request.user)
        cart_count = cart_items.count()
        companylogos = CompanyLogo.objects.all()
        grand_Total = sum(item.total_price for item in cart_items)

        if request.method == "POST":
            billing_name = request.POST.get("billing_name")
            billing_email = request.POST.get("billing_email")
            billing_address = request.POST.get("billing_address")
            billing_phone = request.POST.get("billing_phone")
            billing_message = request.POST.get("billing_message")

            BillingAddress.objects.create(
                billing_name = billing_name,
                billing_email = billing_email,
                billing_address = billing_address,
                billing_phone = billing_phone,
                billing_message = billing_message,
            )

        context = {
            'companylogos':companylogos,
            'cart_count':cart_count,
            'cart_items':cart_items,
            'grand_Total':grand_Total,
        }
        return render(request, "checkout.html", context)
    else:
        return HttpResponse("Please Login First for checkout")

    # return render(request, "checkout.html", context)

def contact(request):
    if request.user.is_authenticated:
        cart_items = Cart.objects.filter(user=request.user)
        cart_count = cart_items.count()
    else:
        cart_items = []
        cart_count =0 

    if request.method == "POST":
        user_name = request.POST.get("user_name")
        user_email = request.POST.get("user_email")
        user_phone = request.POST.get("user_phone")
        user_subject = request.POST.get("user_subject")
        user_message = request.POST.get("user_message")

        UserQuestios.objects.create(
            user_name=user_name,
            user_email=user_email,
            user_phone=user_phone,
            user_subject=user_subject,
            user_message=user_message,
        )
        messages.success(request, "Your query has been submitted successfully!")
        return redirect('contact')  
    return render(request, "contact.html", {'cart_count':cart_count})

def news(request):
    if request.user.is_authenticated:
        cart_items = Cart.objects.filter(user=request.user)
        cart_count = cart_items.count()
    else:
        cart_items = []
        cart_count =0 

    news = productnews.objects.all()
    companylogos = CompanyLogo.objects.all()
    context = {
        'news':news, 
        'companylogos':companylogos,
        'cart_count':cart_count
    }
    return render(request, "news.html", context)

def shop(request):
    if request.user.is_authenticated:
        cart_items = Cart.objects.filter(user=request.user)
        cart_count = cart_items.count()
    else:
        cart_items = []
        cart_count =0 

    companylogos = CompanyLogo.objects.all()
    # product = products.objects.all()[3:] # Get all items after the first 3
    product = products.objects.all() # Get all items after the first 3

    # for paginator --<>
    pg = Paginator(product, 6) 
    page_num = request.GET.get('page')
    page = pg.get_page(page_num)
    context= {
        'products':product, 
        'cart_count':cart_count, 
        "companylogos":companylogos,
        'count':pg.count,
        'page':page,
        'page_num': ceil(pg.count/2)
    }
    return render(request, "shop.html", context)

# def singleNews(request, id):        # by chatgpt
#     # Fetch the specific news item based on its ID
#     news_item = get_object_or_404(productnews, id=id)
#     context = {'news_item': news_item}
#     return render(request, 'single-news.html', context)

def singleNews(request, id):

    if request.user.is_authenticated:
        cart_items = Cart.objects.filter(user=request.user)
        cart_count = cart_items.count()
    else:
        cart_items = []
        cart_count =0 

    companylogos = CompanyLogo.objects.all()
    news_item = get_object_or_404(productnews, id=id)  # Fetch the product by its ID
    # news_item = productnews.objects.get(id=id)  # Fetch the product by its ID
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
           form.save()
           return redirect('singleNews', id=id)
    else:
        initial_data = {'username':'', 'useremail':'', 'comment_text':''}
        form = CommentForm(initial=initial_data)

    comments = Comment.objects.all()
    comment_count = comments.count() 
    # cart_items = Cart.objects.filter(user=request.user)
    # cart_count = cart_items.count()
    context = {
        'news_item': news_item, 
        'comments':comments,
        'form':form, 
        'comment_count':comment_count,
        'companylogos':companylogos,
        'cart_count':cart_count
        }
    return render(request, 'single-news.html', context)

def singlePoduct(request, id):
    product_item = products.objects.get(id=id)  # Fetch the product by its ID
    all_product = products.objects.all()[:3]
    companylogos = CompanyLogo.objects.all()
    cart_items = Cart.objects.filter(user=request.user)
    cart_count = cart_items.count()
    context = {
        'product_item': product_item, 
        'all_product':all_product,
        'companylogos':companylogos,
        'cart_count':cart_count
        }
    return render(request, 'single-product.html', context)



@csrf_exempt
def add_to_cart(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        product_id = data.get('product_id')
        product = products.objects.get(id=product_id)
        user = request.user

        # Check if product is already in cart
        cart_item, created = Cart.objects.get_or_create(user=user, product=product)
        if not created:
            cart_item.quantity += 1
        cart_item.save()

        return JsonResponse({'message': 'Product added to cart successfully!'})
    return JsonResponse({'error': 'Invalid request'}, status=400)




#  For rest framework:
# -- create your own views here
# -- get
# -- post
# -- delete

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import products
from .serializers import Productserializers

class ProductListCreateView(APIView):
    def get(self, request):
        products_list = products.objects.all()
        serializer = Productserializers(products_list, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = Productserializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
