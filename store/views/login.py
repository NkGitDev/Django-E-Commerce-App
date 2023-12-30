from django.shortcuts import render
from django.shortcuts import render, redirect, HttpResponseRedirect
from django.http import HttpResponse
from django.contrib.auth.hashers import make_password, check_password
# from store.models.product import Product
# from store.models.category import Category
from store.models.customer import Customer
from django.views import View



class Login(View):
    return_url = None

    def get(self, request):
        Login.return_url = request.GET.get('return_url')
        return render(request, 'login.html')
    
    def post(self, request):
        rp = request.POST
        email = rp.get('inp_email')
        password = rp.get('inp_password')
        checkCustomer = Customer.get_custmer_by_email(email)
        
        
        error_msg = None
        if checkCustomer:
            flag = check_password(password, checkCustomer.password)
            if flag:
                request.session['customer_id'] = checkCustomer.id
                request.session['email'] = checkCustomer.email

                if Login.return_url:
                    # return HttpResponseRedirect(Login.return_url, {'rtn_msg':return_msg})
                    # or 
                    return redirect(Login.return_url)
                else:
                    Login.return_url = None
                    return redirect('/')
            else:
                error_msg = 'Email or Password Invalid..!'
                return render(request, 'login.html', {'error':error_msg})
        else:
            error_msg = 'Email not exist..!'
            return render(request, 'login.html', {'error':error_msg})
    

def logout(request):
    request.session.clear()
    return redirect('/login/')