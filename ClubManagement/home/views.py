from django.shortcuts import render,redirect
# from django.contrib.auth.models import User
from django.contrib.auth import authenticate,logout,login
from home.models import *
# from .forms import *
from django.contrib import messages
from datetime import datetime
from django.db import connection
# Create your views here.
def index(request):
    return render(request,'index.html')
def signin(request):
    if request.method=="POST":
        #check if user entered correct credentials
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request,user)
            return redirect('/dashboard')
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
def about(request):
    return render(request,'about.html')
def clubmembers(request):
    if request.user.is_authenticated:
        return render(request,'clubmembers.html')
def addmembers(request):
    if request.user.is_authenticated:
        return render(request,'addmembers.html')
def eventslist(request):
    if request.user.is_authenticated:
        return render(request,'eventslist.html')
def addevents(request):
    if request.user.is_authenticated:
        return render(request,'addevents.html')
def clubtimeline(request):
    if request.user.is_authenticated:
        return render(request,'clubtimeline.html')

def dashboard(request):
    if request.user.is_authenticated:
        username=request.user.username
        with connection.cursor() as cursor:
                select_query=f"SELECT CLUB_TYPE,CATEGORY FROM home_clubidentifier where username = '{username}'"
                cursor.execute(select_query)
                result = cursor.fetchall()
                if result:
                    type=result[0][0]
                    category=result[0][1]
        return render(request,'dashboard.html',{"category":category})

def approveRequestOd(request,request_id):
    if request.user.is_authenticated:
        username=request.user.username
        with connection.cursor() as cursor:
                select_query=f"SELECT CLUB_TYPE,CATEGORY FROM home_clubidentifier where username = '{username}'"
                cursor.execute(select_query)
                result = cursor.fetchall()
                if result:
                    type=result[0][0]
                    category=result[0][1]
                    if category=="SC":
                        if type=="cultural":
                            duty_request=OnDutyRequestClubCultural.objects.get(id=request_id)
                            if duty_request:
                                on_duty_sc = OnDutyRequestSCCultural(
                                student_roll_no=duty_request.student_roll_no,
                                date_of_od=duty_request.date_of_od,
                                course_code=duty_request.course_code,
                                faculty_name=duty_request.faculty_name,
                                reason=duty_request.reason)
                                on_duty_sc.save()
                                duty_request.delete()
                                return 
                        elif type=="technical":
                            duty_request=OnDutyRequestClubTechnical.objects.get(id=request_id)
                            if duty_request:
                                on_duty_sc = OnDutyRequestSCTechnical(
                                student_roll_no=duty_request.student_roll_no,
                                date_of_od=duty_request.date_of_od,
                                course_code=duty_request.course_code,
                                faculty_name=duty_request.faculty_name,
                                reason=duty_request.reason)
                                on_duty_sc.save()
                                duty_request.delete()
                                return 
                        elif type=="sports":
                            duty_request=OnDutyRequestClubSports.objects.get(id=request_id)
                            if duty_request:
                                on_duty_sc = OnDutyRequestSCSports(
                                student_roll_no=duty_request.student_roll_no,
                                date_of_od=duty_request.date_of_od,
                                course_code=duty_request.course_code,
                                faculty_name=duty_request.faculty_name,
                                reason=duty_request.reason)
                                on_duty_sc.save()
                                duty_request.delete()
                                return 
                    elif category=="FI":
                        if type=="cultural":
                            duty_request=OnDutyRequestSCCultural.objects.get(id=request_id)
                            if duty_request:
                                duty_request.delete()
                                return 
                        elif type=="technical":
                            duty_request=OnDutyRequestSCTechnical.objects.get(id=request_id)
                            if duty_request:
                                duty_request.delete()
                                return 
                        elif type=="sports":
                            duty_request=OnDutyRequestSCSports.objects.get(id=request_id)
                            if duty_request:
                                duty_request.delete()
                                return 
                else:
                    return
    else:
        return

def approval(request,request_id=None):
    if request.user.is_authenticated:
        username=request.user.username
        with connection.cursor() as cursor:
                select_query=f"SELECT CLUB_TYPE,CATEGORY FROM home_clubidentifier where username = '{username}'"
                cursor.execute(select_query)
                result = cursor.fetchall()
                if result:
                    type=result[0][0]
                    category=result[0][1]
                    print(category,type)
                    if request.method=="POST":
                        if category=="SC":
                            approveRequestOd(request,request_id)
                            if type=="cultural":
                                on_duty_requests = OnDutyRequestClubCultural.objects.all()
                            elif type=="technical":
                                on_duty_requests = OnDutyRequestClubTechnical.objects.all()
                            elif type=="sports":
                                on_duty_requests = OnDutyRequestClubSports.objects.all()
                        elif category=="FI":
                            approveRequestOd(request,request_id)
                            if type=="cultural":
                                on_duty_requests = OnDutyRequestSCCultural.objects.all()
                            elif type=="technical":
                                on_duty_requests = OnDutyRequestSCTechnical.objects.all()
                            elif type=="sports":
                                on_duty_requests = OnDutyRequestSCCultural.objects.all()
                    elif category=="SC" and type=="cultural":
                        #display request list of cultural from clubs
                        print("inside sc and cultural")
                        on_duty_requests = OnDutyRequestClubCultural.objects.all()
                    elif category=="SC" and type=="technical":
                        #display request list of technical from clubs
                        on_duty_requests = OnDutyRequestClubTechnical.objects.all()
                    elif category=="SC" and type=="sports":
                        #display request list of sports from clubs
                        on_duty_requests = OnDutyRequestClubSports.objects.all()
                    elif category=="FI" and type=="cultural":
                        #display request list of sports from sc
                        on_duty_requests = OnDutyRequestSCCultural.objects.all()
                    elif category=="FI" and type=="technical":
                        #display request list of sports from sc
                        on_duty_requests = OnDutyRequestSCTechnical.objects.all()
                    elif category=="FI" and type=="sports":
                        #display request list of sports from sc
                        on_duty_requests = OnDutyRequestSCCultural.objects.all()
                    return render(request, "approval.html", {'on_duty_requests': on_duty_requests})

def requestOnDuty(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            username = request.user.username
            roll_nos = request.POST.getlist('roll_no')
            dates = request.POST.getlist('date')
            course_codes = request.POST.getlist('course-code')
            faculties = request.POST.getlist('faculty')
            reasons = request.POST.getlist('reason')
            with connection.cursor() as cursor:
                select_query=f"SELECT CLUB_TYPE,CATEGORY FROM home_clubidentifier where username = '{username}'"
                cursor.execute(select_query)
                result = cursor.fetchall()
                if result:
                    type=result[0][0]
                    category=result[0][1]
                    if category=="C":
                        if type=="cultural":
                            for i in range(len(roll_nos)):
                                record = OnDutyRequestClubCultural(
                                student_roll_no=roll_nos[i],
                                date_of_od=dates[i],
                                course_code=course_codes[i],
                                faculty_name=faculties[i],
                                reason=reasons[i],
                                )
                                record.save()
                            return redirect('/requestOd')
                        elif type=="sports":
                            for i in range(len(roll_nos)):
                                record = OnDutyRequestClubSports(
                                student_roll_no=roll_nos[i],
                                date_of_od=dates[i],
                                course_code=course_codes[i],
                                faculty_name=faculties[i],
                                reason=reasons[i],
                                )
                                record.save()
                                return redirect('/requestOd')
                        elif type=="technical":
                            for i in range(len(roll_nos)):
                                record = OnDutyRequestClubTechnical(
                                student_roll_no=roll_nos[i],
                                date_of_od=dates[i],
                                course_code=course_codes[i],
                                faculty_name=faculties[i],
                                reason=reasons[i],
                                )
                                record.save()
                                return redirect('/requestOd')
                    elif category=="SC":
                        if type=="cultural":
                            for i in range(len(roll_nos)):
                                record = OnDutyRequestSCCultural(
                                student_roll_no=roll_nos[i],
                                date_of_od=dates[i],
                                course_code=course_codes[i],
                                faculty_name=faculties[i],
                                reason=reasons[i],
                                )
                                record.save()
                                return redirect('/requestOd')
                        elif type=="technical":
                            for i in range(len(roll_nos)):
                                record = OnDutyRequestSCTechnical(
                                student_roll_no=roll_nos[i],
                                date_of_od=dates[i],
                                course_code=course_codes[i],
                                faculty_name=faculties[i],
                                reason=reasons[i],
                                )
                                record.save()
                                return redirect('/requestOd')
                        elif type=="sports":
                            for i in range(len(roll_nos)):
                                record = OnDutyRequestSCCultural(
                                student_roll_no=roll_nos[i],
                                date_of_od=dates[i],
                                course_code=course_codes[i],
                                faculty_name=faculties[i],
                                reason=reasons[i],
                                )
                                record.save()
                                return redirect('/requestOd')
    return render(request,"requestOd.html")