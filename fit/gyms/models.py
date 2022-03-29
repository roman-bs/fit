from django.conf import settings
from django.db import models


class Сlient(models.Model):
    title = models.CharField(max_length=200)
    name = models.TextField()
    age = models.IntegerField()
    weight = models.IntegerField()
    age = models.IntegerField()
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return f'{self.name} {self.age}'





class Сoach(models.Model):
    title = models.CharField(max_length=200)
    name = models.TextField()
    route = models.TextField()
    gyms = models.ManyToManyField('Gym')
    #training_programs = models.ForeignKey(Training_program, on_delete = models.CASCADE)
    clients = models.ManyToManyField(Сlient)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return f'{self.name} {self.route}'

class Gym(models.Model):
    title = models.CharField(max_length=200)
    address = models.TextField()
    image = models.ImageField(null=True, blank=True)
    square = models.TextField()
    text = models.TextField()
    сoachs = models.ManyToManyField(Сoach)

    def __str__(self):
        return f'{self.address} {self.square}'


class Diet(models.Model):
    author = models.ForeignKey(
        Сoach, on_delete=models.CASCADE, related_name="diet"
    )
    text = models.TextField()
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.author


class Tags(models.Model):
    title = models.CharField(max_length=100)
    gyms = models.ManyToManyField(Gym)

