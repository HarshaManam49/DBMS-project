from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout

# Create your views here.
def index(request):
    return render(request,'index.html')
def signin(request):
    return render(request,'signin.html')
def contact(request):
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
