from django.db import models

from django.db import models
from django.conf import settings
from django.core.urlresolvers import reverse

class Category(models.Model):
    title = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse('blog:category_detail', args=[self.pk])

class Shop(models.Model):
    category = models.ForeignKey(Category)
    title = models.CharField(max_length=100)
    number = models.CharField(max_length=20)
    address = models.CharField(max_length=100)
    about = models.TextField()
    photo1 = models.ImageField()
    photo2 = models.ImageField(blank=True)
    photo3 = models.ImageField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse('blog:shop_detail', args=[self.pk])

class Review(models.Model):
    shop = models.ForeignKey(Shop)
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    message = models.TextField()
    photo = models.ImageField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)