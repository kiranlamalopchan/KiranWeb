from django.shortcuts import redirect


def auth_middleware(get_response):
    def middleware(request):
        username = request.session.get('userid')
        returnUrl = request.META['PATH_INFO']
        if not username:
            return redirect(f'/customers/login?return_url={returnUrl}')
        response = get_response(request)

        return response

    return middleware
