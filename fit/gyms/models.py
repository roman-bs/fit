from django.conf import settings
from django.db import models


class Gym(models.Model):
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="posts"
    )
    title = models.CharField(max_length=200)
    image = models.ImageField(blank=True, null=True)
    slug = models.SlugField()
    text = models.TextField()
    title = models.CharField(max_length=200)
    created_at = models.DateTimeField(
        auto_now_add=True, db_index=True
    )


class Tags(models.Model):
    title = models.CharField(max_length=100)
    gyms = models.ManyToManyField(Gym)