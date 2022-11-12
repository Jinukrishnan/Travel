from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


def register(request):
    if request.method == 'POST':
        User_name = request.POST['user_name']
        First_name = request.POST['first_name']
        Last_name = request.POST['last_name']
        email = request.POST['email']
        pwd = request.POST['pwd']
        cnfpwd = request.POST['cnfpwd']
        if pwd == cnfpwd:
            if User.objects.filter(username=User_name).exists():
                messages.info(request, "Username Already Taken")
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, "Email Already Taken")
                return redirect('register')
            else:
                user = User.objects.create_user(username=User_name, password=pwd, first_name=First_name,
                                                last_name=Last_name, email=email)
                user.save()

        else:
            messages.info(request, "Check and verify Your Pass word")
            return redirect('register')
        return redirect('/')
    return render(request, 'register.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        pwd = request.POST['pwd']
        user = auth.authenticate(username=username, password=pwd)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,'Invalid Entry')
            return redirect('login')
    return render(request, 'login.html')

def logout(request):
    auth.logout(request)
    return redirect('/')

