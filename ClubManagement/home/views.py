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
    if request.method == 'POST':
        roll_nos = request.POST.getlist('roll_no')
        dates = request.POST.getlist('date')
        course_codes = request.POST.getlist('course-code')
        faculties = request.POST.getlist('faculty')
        reasons = request.POST.getlist('reason')

        # Now you can process the data, e.g., save it to a model
        # Loop through the lists and create records in your model
        for i in range(len(roll_nos)):
            roll_no = roll_nos[i]
            date = dates[i]
            course_code = course_codes[i]
            faculty = faculties[i]
            reason = reasons[i]
            print(roll_no," ",date," ",course_code," ",faculty," ",reason)

    return render(request,'addevents.html',{})
def clubtimeline(request):
    return render(request,'clubtimeline.html')
def requestOd(request):
    if request.method == 'POST':
        roll_nos = request.POST.getlist('roll_no[]')
        dates = request.POST.getlist('date[]')
        course_codes = request.POST.getlist('course_code[]')
        faculties = request.POST.getlist('faculty[]')
        reasons = request.POST.getlist('reason[]')

        # Now you can process the data, e.g., save it to a model
        # Loop through the lists and create records in your model
        for i in range(len(roll_nos)):
            roll_no = roll_nos[i]
            date = dates[i]
            course_code = course_codes[i]
            faculty = faculties[i]
            reason = reasons[i]
            print(roll_no," ",date," ",course_code," ",faculty," ",reason)
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
def profile(request):
    return render(request,'profile.html')
def changepasswd(request):
    return render(request,'changepasswd.html')
