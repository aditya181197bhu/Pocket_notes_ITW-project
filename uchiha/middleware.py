from django.http import HttpResponse

def ipfilter(get_response):
    def middleware(request):
        allowed_ips=['127.0.0.1']
        ip=request.META.get('REMOTE_ADDR')
        ip1=ip.split('.')
        if ip1[2]!='52' :
            allowed_ips.append(ip)
        print(ip)
        if ip not in allowed_ips:
            return HttpResponse('Hold On!.... You are not from IIT BHU!!')
        response=get_response(request)
        return response
    return middleware