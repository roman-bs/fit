from django.conf import settings
from django.db import models


class Trainer(models.Model):
    title = models.CharField(max_length=200)
    name = models.TextField()
    route = models.TextField()
    gyms = models.ManyToManyField('Gym')
    clients = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="clients")
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return f'{self.name} {self.route}'


class Program(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(
        Trainer, on_delete=models.CASCADE, related_name="programs"
    )
    image = models.ImageField(blank=True, null=True)
    slug = models.SlugField()
    text = models.TextField()

    def __str__(self):
        return f'{self.title} {self.author}'


class Gym(models.Model):
    title = models.CharField(max_length=200)
    address = models.TextField()
    image = models.ImageField(null=True, blank=True)
    square = models.TextField()
    text = models.TextField()
    trainers = models.ManyToManyField(Trainer)

    def __str__(self):
        return f'{self.address} {self.square}'


class Diet(models.Model):
    author = models.ForeignKey(
        Trainer, on_delete=models.CASCADE, related_name="diet"
    )
    text = models.TextField()
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.author


class Tags(models.Model):
    title = models.CharField(max_length=100)
    gyms = models.ManyToManyField(Gym)
