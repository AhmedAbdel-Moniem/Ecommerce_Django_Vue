from django.db import models
from django.urls import reverse

# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250)
    ordering = models.IntegerField(default=0)
    class Meta:
        verbose_name_plural = 'Categories'
        ordering = ('ordering',)
    
    def __str__(self):
        return self.title
    
    
class Product(models.Model):
    category = models.ForeignKey(Category, related_name="products", on_delete=models.CASCADE)
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=5, decimal_places=2)
    date_created = models.DateTimeField(auto_now_add=True)
    is_featured = models.BooleanField(default=True)
    
    
    class Meta:
        ordering = ('-date_created',)
    def __str__(self):
        return self.title
    
    # def get_absolute_url(self):
    #     return reverse('product_details', kwargs={"slug": "slug"})