from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate 
from django.contrib.auth import logout,login
from home.models import Contact
from django.contrib import messages
from datetime import datetime
# Create your views here.
def index(request):
    return render(request,'index.html')
def signin(request):
    if request.method=="POST":
        #check if user entered correct credentials
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username,password)
        user = authenticate(username=username, password=password)

        if user is not None:
            login(request,user)
            return render(request,'dashboard.html')
        else:
            print("yes")
            return render(request,"signin.html")
    return render(request,'signin.html')
def signout(request):
    logout(request)
    return redirect("/")
def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        contact = Contact(name=name, email=email, phone=phone, desc=desc, date = datetime.today())
        contact.save()
        messages.success(request, 'Your message has been sent!')
    return render(request,'contact.html')
def dashboard(request):
    return render(request,'dashboard.html')
