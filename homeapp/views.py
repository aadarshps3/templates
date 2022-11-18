from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login

# Create your views here.
def mainpage(request):
    return render(request,'index1.html')

def loginpage(request):
    if request.method=='POST':
        username=request.POST.get('uname')
        password=request.POST.get('pass')
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            if user.is_staff:
                return redirect('adminpage')
        else:
            messages.info(request,'invalid credentials')
    return render(request,'login.html')

def register(request):
    return render(request,'register.html')

def adminpage(request):
    return render(request,'inindexadm.html')

def user(request):
    return render(request,'user.html')

def worker(request):
    return render(request,'worker.html')


