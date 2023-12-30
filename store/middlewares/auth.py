from django.shortcuts import redirect

def auth_middleware(get_response):

    def middleware(request):
        # print('my middleware...')
        returnUrl = request.META['PATH_INFO']
        if not request.session.get('customer_id'):
            return redirect(f'/login?return_url={returnUrl}')
        response = get_response(request)
        return response
    return middleware

def del_middleware(get_response):
    def middleware2(request, id):
        returnUrl = request.META['PATH_INFO']
        if request.session.get('customer_id'):
            return redirect(f'/cart?return_url={returnUrl}')
        response = get_response(request, id)
        return response
    return middleware2