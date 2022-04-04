from django.conf import settings
from django.db import models


class Trainer(models.Model):
    title = models.CharField(max_length=200)
    name = models.TextField()
    route = models.TextField()
    gyms = models.ManyToManyField('Gym', blank=True)
    clients = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="trainer", blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return f'{self.name} {self.route}'


class Gym(models.Model):
    name = models.TextField()
    title = models.CharField(max_length=200)
    address = models.TextField()
    image = models.ImageField(null=True, blank=True)
    square = models.TextField()
    text = models.TextField()
    trainers = models.ManyToManyField(Trainer, blank=True)

    def __str__(self):
        return self.name


class Program(models.Model):
    author = models.ForeignKey(
        Trainer, on_delete=models.CASCADE, related_name="diet"
    )
    text = models.TextField()
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title


class Tags(models.Model):
    title = models.CharField(max_length=100)
    gyms = models.ManyToManyField(Gym)


class Product(models.Model):
    author = models.ForeignKey(
        Gym, on_delete=models.CASCADE, related_name="product")
    title = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Цена')
    text = models.TextField()

    def __str__(self):
        return f"{self.title} - {self.price}"


class Order(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='orders', verbose_name="Заказы"
    )
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    purchase = models.ForeignKey(
        Product, related_name="purchases", on_delete=models.CASCADE, null=True,
    )
    count = models.IntegerField(null=True)
    cost = models.DecimalField(decimal_places=2, max_digits=250, default=0)
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    updated = models.DateTimeField(auto_now=True, db_index=True)
    paid = models.BooleanField(default=False)

    class Meta:
        ordering = ('-created_at',)
        verbose_name = 'Order'
        verbose_name_plural = 'Order'

    def __str__(self):
        return f"Order №{self.id}"

    def get_cost(self):
        return self.cost * self.count
