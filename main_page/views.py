from django.shortcuts import render,redirect
from . models import Category, Product, Cart
from . import models
from .forms import SearchForm
from telebot import TeleBot

bot = TeleBot('6035375977:AAHSpVSCGNzx_uL3JTctr2L_d74Z931VqZo', parse_mode='HTML')


# Create your views here.
def index(request):
    # taking all category of products from db
    all_categories = models.Category.objects.all()
    all_products = models.Product.objects.all()

    search_bar = SearchForm()
    context = {'products': all_products, 'all_categories': all_categories, 'form':search_bar}

    if request.method == 'POST':
        product_find = request.POST.get('search_product')
        try:
            search_result = models.Product.objects.get(product_name=product_find)
            return redirect(f'/item/{search_result.id}')
        except:
            return redirect('/')
    return render(request, 'index.html', context)

"""    from_frontend = request.GET.get('exact_product')
    if from_frontend is not None:
        # in this case creating dynamic url
        all_products = models.Product.objects.filter(product_name__contains=from_frontend)
"""
    # making a dictionary for correct display in front end


    # return rendered version to front


# getting redirect from index function to item/ page, in urls 'item' using this function in order to pass it to frontend, with id of product
def exact_product(request, pk):
    find_product_from_db = models.Product.objects.get(id=pk)
    context = {'products':find_product_from_db}
    return render(request, 'exact_product.html', context)

def get_exact_category(request, pk):
    # get single object from db by id
    exact_category = models.Category.objects.get(id=pk)
    #  using filter picking all product data by filter
    category_products = models.Product.objects.filter(product_category=exact_category)

    return render(request, 'exact_category.html', {'category_products':category_products})


def get_exact_product(request, pk):
    product = models.Product.objects.get(id=pk)
    context = {'product': product}
    if request.method == 'POST':
        models.Cart.objects.create(user_id=request.user.id,
                    user_product=product,
                    user_product_quantity=request.POST.get('user_product_quantity'),
            total_for_product=product.product_price*int(request.POST.get('user_product_quantity')))
        return redirect('/cart')

    return render(request, 'exact_product.html', context)

def get_user_cart(request):
    user_cart = models.Cart.objects.filter(user_id=request.user.id)
    context = {'cart':user_cart}
    return render(request, 'user_cart.html', context)

# submit order
def complete_order(request):
    user_cart = models.Cart.objects.filter(user_id=request.user.id)

    # preraring message for telegram admin
    result_message = "new order(site)\n\n"
    # total count of products
    total_for_all_cart = 0
    for cart in user_cart:
        result_message += f'<b>{cart.user_product}</b> x {cart.user_product_quantity} = {cart.total_for_product} sum\n'

        total_for_all_cart += total_for_all_cart

    result_message += f"\n-------------\n<b>total: {total_for_all_cart} sum</b>"
    # message for admin to telegram
    bot.send_message(74682627, result_message)
    return redirect('/')