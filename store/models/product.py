from django.db import models
from .category import Category


# Create your models here.
class Product(models.Model):
    prod_name = models.CharField(max_length=80)
    prod_price = models.IntegerField(default=0)
    prod_category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
    prod_desc = models.CharField(max_length=200, default='', null=True, blank=True)
    prod_img = models.ImageField(upload_to='products_images/')


    def __str__(self) -> str:
        return self.prod_name

    @staticmethod
    def get_all_products():
        return Product.objects.all()
    
    @staticmethod
    def get_all_products_by_categoryId(category_id):
        if category_id:
            return Product.objects.filter(prod_category = category_id)
        else:
            return Product.objects.all()
        
    @staticmethod
    def get_product_by_id(ids):
        return Product.objects.filter(id__in = ids)
    
    @staticmethod
    def remove_product(prd_id):
        return Product.objects.filter(id__in = prd_id)