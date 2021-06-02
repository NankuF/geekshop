from django.db import models


class ProductCategory(models.Model):
    name = models.CharField(max_length=128, unique=True, blank=False)
    description = models.TextField(max_length=256, blank=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=64, unique=True, blank=False)
    image = models.ImageField(upload_to='products_images')  # default blank=False ?? yes!
    description = models.CharField(max_length=128, blank=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    quantity = models.PositiveIntegerField(default=0)

    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.name} | {self.category.name}'
