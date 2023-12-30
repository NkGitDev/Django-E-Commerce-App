from django.shortcuts import render
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.hashers import make_password, check_password
# from store.models.product import Product
# from store.models.category import Category
from store.models.customer import Customer
from django.views import View



class SignUp(View):
    def get(self, request):
        return render(request, 'signup.html')
    
    def post(self, request):
        rp = request.POST
        firstName = rp.get('inp_firstname')
        lastName = rp.get('inp_lastname')
        mobile = rp.get('inp_mobile')
        email = rp.get('inp_email')
        password = rp.get('inp_password')


        # Re-Get Values in input fields
        values = {
            'firstName':firstName,
            'lastName':lastName,
            'mobile':mobile,
            'email':email
        }
        
        custData = Customer(
                first_name = firstName,
                last_name = lastName,
                mobile = mobile,
                email = email,
                password = password
            )
        
        error_msg = None


        error_msg = self.validate_user(custData)

        if not error_msg:
            # password hashing
            custData.password = make_password(custData.password)
            # custom method from customer model 
            custData.register()

            # # or we can use this also
            # custData.save()

            # redirect after save data 
            # msg = 'Successfull saved data...'
            return redirect('/')

        else:
            data = {
                'error':error_msg,
                'values':values
            }
            return render(request, 'signup.html', data)

    def validate_user(self, cust):
        # Validation
        error_msg = None
        if not cust.first_name:
            error_msg = 'First Name is required..!'
        elif len(cust.first_name) < 3:
            error_msg = 'First Name must be min. 3 character.'
        elif not cust.last_name:
            error_msg = 'Last Name is required..!'
        elif not cust.mobile:
            error_msg = 'Mobile number is required..!'
        elif len(cust.mobile) < 10:
            error_msg = 'Mobile number must be 10 digit.'
        elif not cust.email:
            error_msg = 'Please enter a valid email..!'
        elif not cust.password:
            error_msg = 'Please fill the password.'
        elif len(cust.password) < 8:
            error_msg = 'Password must be min. 8 character or digit'
        # check email exist or not manually
        elif cust.emailIsExist():
            error_msg = 'Email Already Exist. please enter another email'
        
        return error_msg