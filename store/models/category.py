from django.db import models

class Category(models.Model):
    cat_name = models.CharField(max_length=20)


    def get_all_categories():
        return Category.objects.all()

    def __str__(self) -> str:
        return self.cat_name