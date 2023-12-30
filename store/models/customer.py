from django.db import models

class Customer(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    mobile = models.IntegerField()
    email = models.EmailField()
    password = models.CharField(max_length=200)


    def __str__(self) -> str:
        return self.first_name

    def register(self):
        self.save()

    # check email already exist
    def emailIsExist(self):
        if Customer.objects.filter(email = self.email):
            return True
        else:
            return False

    def get_custmer_by_email(email):
        try:
            return Customer.objects.get(email = email)
        except:
            return False
        
    # def get_customer_by_name(name):
    #     try:
    #         return Customer.objects.get(first_name = name)
    #     except:
    #         return False