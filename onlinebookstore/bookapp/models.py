from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Book(models.Model):
    title = models.CharField(max_length=400)
    author = models.CharField(max_length=400)
    description = models.TextField()
    price = models.DecimalField(decimal_places=3, max_digits=5)
    image_url = models.CharField(max_length=2000, blank=True, default=False)
    book_available = models.BooleanField(blank=False)


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    items = models.ManyToManyField(Book)
    total_price = models.DecimalField(max_digits=10, decimal_places=5)


class CartItems(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def total_price(self):
        return self.book.price * self.quantity