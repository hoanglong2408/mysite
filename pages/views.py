from django.http import HttpResponse

def about(request):
    return HttpResponse("Đây là trang giới thiệu")
