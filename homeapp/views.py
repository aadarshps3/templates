from django.shortcuts import render

# Create your views here.
def mainpage(request):
    return render(request,'index1.html')

def loginpage(request):
    return render(request,'login.html')

def register(request):
    return render(request,'register.html')

def adminpage(request):
    return render(request,'inindexadm.html')