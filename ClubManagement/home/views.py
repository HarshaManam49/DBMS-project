from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate 
from django.contrib.auth import logout,login
from home.models import Contact
from django.contrib import messages
from datetime import datetime
# Create your views here.
def index(request):
    if request.user.is_anonymous:
        return redirect("/signin")
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
            return redirect("/")
        else:
            print("yes")
            return render(request,"signin.html")
    return render(request,'signin.html')
def signout(request):
    logout(request)
    return redirect("/signin")
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
def about(request):
    return render(request,'about.html')
def dashboard(request):
    return render(request,'dashboard.html')
def clubmembers(request):
    return render(request,'clubmembers.html')
def addmembers(request):
    return render(request,'addmembers.html')
def eventslist(request):
    return render(request,'eventslist.html')
def addevents(request):
    return render(request,'addevents.html')
def clubtimeline(request):
    return render(request,'clubtimeline.html')
def requestOd(request):
    return render(request,'requestOd.html')
def signin(request):
    if request.method=="POST":
        #check if user entered correct credentials
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username,password)
        user = authenticate(username=username, password=password)

        if user is not None:
            print("yes1")
            login(request,user)
            context={
                "username":username
            }
            return render(request,"dashboard.html",context)
        else:
            print("yes")
            return render(request,"signin.html")
    else:
        return render(request,'signin.html')
def signout(request):
    logout(request)
    return redirect("/")
