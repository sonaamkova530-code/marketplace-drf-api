from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator

class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name="Назва товару")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Ціна")
    description = models.TextField(verbose_name="Опис")
    is_active = models.BooleanField(default=True, verbose_name="Активний")
    image = models.ImageField(upload_to="products_images/", null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата створення")
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name="products", verbose_name="Власник")

    def __str__(self):
        return f"{self.name} - {self.price} грн (Власник {self.owner.username})"


class Review(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="reviews")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    text = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.rating} для {self.product.name} від {self.user.username}"
