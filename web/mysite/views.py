from django.http import HttpResponse
from django.shortcuts import render
from .models import user


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


def UserRegPage(request):
    return render(request, 'userreg.html')


def UserRegistered(request):
    fname = request.POST.get('fname')
    lname = request.POST.get('lname')
    dept = request.POST.get('department')
    email = request.POST.get('email')
    mobile = request.POST.get('mobile')
    username = request.POST.get('username')
    password = request.POST.get('password')
    div = request.POST.get('division')
    userObject = user(fname=fname, lname=lname, department=dept, email=email, mobile=mobile, username=username,
                      password=password, division=div)
    userObject.save()
    print("user's data saved succesfully")
    return HttpResponse("registration succesfull")


def UserLoginPage(request):
    return render(request, 'login.html')


def AuthUser(request):
    username = request.POST.get('username')
    print(username)
    password = request.POST.get('password')
    fetchuserdata = user.objects.filter(username=username, password=password)
    if fetchuserdata:
        for i in fetchuserdata:
            if i.username == username:
                print(username)
                print(i.username)
                return HttpResponse("Authenticate succesfully")
            else:
                return HttpResponse("Authentication failed")
    else:
        return HttpResponse("Authentication failed")
