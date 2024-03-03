from django.db import models

class Category(models.Model):
    category_name = models.CharField(max_length=100)
    name = models.CharField(max_length=10)
    slug = models.SlugField(unique=True, null=True, blank=True)
    category_image = models.ImageField(upload_to="categories")

class Product(models.Model):
    product_name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="products")
    slug = models.SlugField(unique=True, null=True, blank=True)
    price = models.IntegerField()
    product_description = models.TextField()

class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="product_images")
    image = models.ImageField(upload_to="product")
