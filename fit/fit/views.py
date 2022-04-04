import logging

from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.shortcuts import render, get_object_or_404
from gym.models import Product
from cart.forms import CartAddProductForm

from fit.forms import RegisterForm

logger = logging.getLogger(__name__)


def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            # Process validated data
            logger.info(form.cleaned_data)
            user = User(
                username=form.cleaned_data['email'],
                email=form.cleaned_data['email'],
                first_name=form.cleaned_data['first_name'],
                last_name=form.cleaned_data['last_name'],
            )
            user.set_password(form.cleaned_data['password'])
            user.save()
            return redirect("home")
    else:
        form = RegisterForm()
    return render(request, "authentication/registration.html", {"form": form})


def product_detail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    cart_product_form = CartAddProductForm()
    return render(request, 'cart/detail.html', {'product': product,
                                                "cart_product_form": cart_product_form})