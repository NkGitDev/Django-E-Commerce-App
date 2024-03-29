from django.contrib import admin
from .models.product import Product
from .models.category import Category
from .models.customer import Customer
from .models.orders import Orders


# Register your models here.
class AdminProduct(admin.ModelAdmin):
    list_display = ['prod_name', 'prod_price', 'prod_category', 'prod_desc', 'prod_img']

class AdminCategory(admin.ModelAdmin):
    list_display = ['cat_name']



admin.site.register(Product, AdminProduct)
admin.site.register(Category, AdminCategory)
admin.site.register(Customer)
admin.site.register(Orders)