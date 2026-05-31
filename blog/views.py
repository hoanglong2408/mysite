from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    hoTen = "Long Trần"
    diem = [8,6,10]  # Toán, lý, hóa
    return render(request,'blog/home.html',{
        'username':hoTen,
        'grades':diem
        })

def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        return render(request,'blog/register.html',{
            'username': username,
            'password': password
    })
    return render(request,'blog/register.html')



