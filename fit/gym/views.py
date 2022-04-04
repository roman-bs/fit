import logging
from django.shortcuts import render, get_object_or_404, redirect

from cart.cart import Cart
from cart.forms import CartAddProductForm
from gym.forms import OrderForm
from gym.models import Gym, Trainer, Product, Order

logger = logging.getLogger(__name__)


def gym_list(request):
    gyms = Gym.objects.order_by("-id")
    return render(request, "gyms/list_gyms.html", {"gyms": gyms})


def gym_view(request, gym_id):
    gym = Gym.objects.get(id=gym_id)
    return render(request, "gyms/card.html", {"gym": gym})


def trainer_list(request):
    trainers = Trainer.objects.order_by("-id")
    return render(request, "trainers/list_trainer.html", {"trainers": trainers})


def trainer_view(request, trainer_id):
    trainer = Trainer.objects.get(id=trainer_id)
    return render(request, "trainers/trainer_card.html", {"trainer": trainer})


def product_list(request):
    products = Product.objects.order_by("-id")
    return render(request, "product/product_list.html", {"products": products})


def product_view(request, product_id):
    product = Product.objects.get(id=product_id)
    return render(request, "product/product_card.html", {"product": product})


def product_details_view(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    product_cart_form = CartAddProductForm()
    return render(request, "product/details.html",
                  {"product": product, 'product_cart_form': product_cart_form})


def order_list(request):
    cart = Cart(request)
    if request.user.is_authenticated:
        if request.method == "POST":
            form = OrderForm(request.POST)
            if form.is_valid():
                order = []
                logger.info(form.cleaned_data)
                for item in cart:
                    ordr = Order.objects.create(purchase=item['product'],
                                                cost=item['price'],
                                                count=item['quantity'],
                                                user=request.user,
                                                first_name=form.cleaned_data['first_name'],
                                                last_name=form.cleaned_data['last_name'],
                                                email=form.cleaned_data['email'])

                    ordr.save()
                    order.append(ordr)
                cart.clear()
                return render(request, 'product/order_created.html',
                              {'order': order})
        else:
            form = OrderForm()
    else:
        return redirect('/login/', )
    return render(request, 'product/order_create.html',
                  {'cart': cart, 'form': form})


def history_list(request):
    product = Product.objects.all()
    order = Order.objects.filter(user=request.user)
    return render(request, "product/history.html", {"order": order, "product": product})
