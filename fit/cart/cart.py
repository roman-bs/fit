from decimal import Decimal
from django.conf import settings
from gym.models import Product


class Cart(object):

    def __init__(self, request):
        """
        Инициализация корзины
        """
        self.session = request.session
        cart = self.session.get(settings.CART_SESSION_ID)
        if not cart:
            # сохранение пустой корзины в сессии
            cart = self.session[settings.CART_SESSION_ID] = {}
        self.cart = cart


    def __iter__(self):
        """
        переборка товара в корзине и получение товара из бд
        """
        product_ids = self.cart.keys()
        # получаем товары и добавляем их в корзину
        products = Product.objects.filter(id__in=product_ids)

        cart = self.cart.copy()
        for product in products:
            cart[str(product.id)]['product'] = product

        for item in cart.values():
            item['price'] = Decimal(item['price'])
            item['total_price'] = item['price'] * item['quantity']
            yield item

    def __len__(self):
        '''
        подсчет товара в корзине
        '''
        return sum(item['quantity'] for item in self.cart.values())

    def add(self, product, quantity=1, update_quantity=False):
        """
        добавление товара в корзину или обновление его количества
        """
        product_id = str(product.id)
        if product_id not in self.cart:
            self.cart[product_id] = {'quantity': 0,
                                     'price': str(product.price)}
        if update_quantity:
            self.cart[product_id]['quantity'] = quantity
        else:
            self.cart[product_id]['quantity'] += quantity
        self.save()


    def save(self):
        #сщхранение товара
        self.session.modified = True


    def remove(self, product):
        """
        удаление товара
        """
        product_id = str(product.id)
        if product_id in self.cart:
            del self.cart[product_id]
            self.save()


    def get_total_price(self):
        # получение общей стоимости
        return sum(Decimal(item['price']) * item['quantity'] for item in self.cart.values())


    def clear(self):
        # очистка корзины в сессии
        del self.session[settings.CART_SESSION_ID]
        self.save()