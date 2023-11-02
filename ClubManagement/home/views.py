from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,logout,login
from home.models import *
from django.contrib import messages
from datetime import datetime
from django.db import connection
from django.views.decorators.cache import cache_control
from datetime import datetime
from datetime import time
from datetime import timedelta
from .models import Events
from .models import  Contact,upcomming_events,get_all_member,get_club_name,is_slot_free,update_status_of_events,get_all_events,get_all_completed_events
from .models import  get_all_coordinators,get_faculty_name
from .models import music,dance,finearts,yoga,ebsb,literaryanddebating
from .models import media,photography,netsec,webdev,competitivecoding,iot,robotics,circopt,science,volleyball,cricket
from .models import badminton,tabletennis,basketball,carrom,chess,kabbadi,athleticstrack,athleticsfield,football,throwball




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
    objs=[]
    if request.user.is_authenticated:
        username=request.user.username
        with connection.cursor() as cursor:
                select_query=f"SELECT CLUB_TYPE,CATEGORY FROM home_clubidentifier where username = '{username}'"
                cursor.execute(select_query)
                result = cursor.fetchall()
                if result:
                    category=result[0][1]
        club_name=get_club_name(username)
        club_name=club_name[0][0]
        objs=get_all_member(club_name)
        return render(request,'clubmembers.html',{'objs' : objs,'category':category})

def addmembers(request):
    if request.user.is_authenticated:
        username=request.user.username
        with connection.cursor() as cursor:
                select_query=f"SELECT CLUB_TYPE,CATEGORY FROM home_clubidentifier where username = '{username}'"
                cursor.execute(select_query)
                result = cursor.fetchall()
                if result:
                    category=result[0][1]
        if request.method=="POST" :
            roll=request.POST.get('roll')
            roll=int(roll)
            name=request.POST.get('name') 
            joining_year=request.POST.get('joining_year')
            joining_year=int(joining_year)
            designation=request.POST.get('designation')
            designation=designation.lower()
            branch=request.POST.get('branch')
            branch=branch.lower()
            club_name=get_club_name(username)
            club_name=club_name[0][0]
            if club_name=="music" :
                    obj=music(roll=roll,name=name,joining_year=joining_year,designation=designation,branch=branch)
                    obj.save()
            elif club_name=="dance" :
                    obj=dance(roll=roll,name=name,joining_year=joining_year,designation=designation,branch=branch)
                    obj.save()
            elif club_name=="finearts" :
                    obj=finearts(roll=roll,name=name,joining_year=joining_year,designation=designation,branch=branch)
                    obj.save()
            elif club_name=="yoga" :
                    obj=yoga(roll=roll,name=name,joining_year=joining_year,designation=designation,branch=branch)
                    obj.save()
            elif club_name=="ebsb" :
                    obj=ebsb(roll=roll,name=name,joining_year=joining_year,designation=designation,branch=branch)
                    obj.save()
            elif club_name=="literaryanddebating" :
                    obj=literaryanddebating(roll=roll,name=name,joining_year=joining_year,designation=designation,branch=branch)
                    obj.save()
            elif club_name=="media" :
                    obj=media(roll=roll,name=name,joining_year=joining_year,designation=designation,branch=branch)
                    obj.save()
            elif club_name=="photography" :
                    obj=photography(roll=roll,name=name,joining_year=joining_year,designation=designation,branch=branch)
                    obj.save()
            elif club_name=="netsec" :
                    obj=netsec(roll=roll,name=name,joining_year=joining_year,designation=designation,branch=branch)
                    obj.save()
            elif club_name=="webdev" :
                    obj=webdev(roll=roll,name=name,joining_year=joining_year,designation=designation,branch=branch)
                    obj.save()
            elif club_name=="competitivecoding" :
                    obj=competitivecoding(roll=roll,name=name,joining_year=joining_year,designation=designation,branch=branch)
                    obj.save()
            elif club_name=="iot" :
                    obj=iot(roll=roll,name=name,joining_year=joining_year,designation=designation,branch=branch)
                    obj.save()
            elif club_name=="robotics" :
                    obj=robotics(roll=roll,name=name,joining_year=joining_year,designation=designation,branch=branch)
                    obj.save()
            elif club_name=="circopt" :
                    obj=circopt(roll=roll,name=name,joining_year=joining_year,designation=designation,branch=branch)
                    obj.save()
            elif club_name=="science" :
                    obj=science(roll=roll,name=name,joining_year=joining_year,designation=designation,branch=branch)
                    obj.save()
            elif club_name=="volleyball" :
                    obj=volleyball(roll=roll,name=name,joining_year=joining_year,designation=designation,branch=branch)
                    obj.save()
            elif club_name=="cricket" :
                    obj=cricket(roll=roll,name=name,joining_year=joining_year,designation=designation,branch=branch)
                    obj.save()
            elif club_name=="badminton" :
                    obj=badminton(roll=roll,name=name,joining_year=joining_year,designation=designation,branch=branch)
                    obj.save()
            elif club_name=="tabletennis" :
                    obj=tabletennis(roll=roll,name=name,joining_year=joining_year,designation=designation,branch=branch)
                    obj.save()
            elif club_name=="basketball" :
                    obj=basketball(roll=roll,name=name,joining_year=joining_year,designation=designation,branch=branch)
                    obj.save()
            elif club_name=="carrom" :
                    obj=carrom(roll=roll,name=name,joining_year=joining_year,designation=designation,branch=branch)
                    obj.save()
            elif club_name=="chess" :
                    obj=chess(roll=roll,name=name,joining_year=joining_year,designation=designation,branch=branch)
                    obj.save()
            elif club_name=="kabbadi" :
                    obj=kabbadi(roll=roll,name=name,joining_year=joining_year,designation=designation,branch=branch)
                    obj.save()
            elif club_name=="athleticstrack" :
                    obj=athleticstrack(roll=roll,name=name,joining_year=joining_year,designation=designation,branch=branch)
                    obj.save()
            elif club_name=="athleticsfield" :
                    obj=athleticsfield(roll=roll,name=name,joining_year=joining_year,designation=designation,branch=branch)
                    obj.save()
            elif club_name=="football" :
                    obj=football(roll=roll,name=name,joining_year=joining_year,designation=designation,branch=branch)
                    obj.save()
            elif club_name=="throwball" :
                    obj=throwball(roll=roll,name=name,joining_year=joining_year,designation=designation,branch=branch)
                    obj.save()
            messages.success(request,"Added Successfully")
        return render(request,'addmembers.html',{'category':category})

def eventslist(request):
    if request.user.is_authenticated:
        username=request.user.username
        with connection.cursor() as cursor:
                select_query=f"SELECT CLUB_TYPE,CATEGORY FROM home_clubidentifier where username = '{username}'"
                cursor.execute(select_query)
                result = cursor.fetchall()
                if result:
                    category=result[0][1]
        club_name=get_club_name(username)
        club_name=club_name[0][0]
        update_status_of_events()
        events=upcomming_events(club_name)
        return render(request,'eventslist.html',{'events' : events,'category':category})

        
def addevents(request):
    if request.user.is_authenticated:
        username=request.user.username
        with connection.cursor() as cursor:
                select_query=f"SELECT CLUB_TYPE,CATEGORY FROM home_clubidentifier where username = '{username}'"
                cursor.execute(select_query)
                result = cursor.fetchall()
                if result:
                    category=result[0][1]
        if request.method=="POST" :
            name=request.POST.get('name')
            my_date=request.POST.get('date')
            my_date = datetime.strptime(my_date, '%Y-%m-%d').date()
            my_time=request.POST.get('time')
            my_time=my_time.split(':')
            hours=int(my_time[0])
            minutes=int(my_time[1])
            my_time=time(hours,minutes)
            venue=request.POST.get('venue')
            status=request.POST.get('status')
            end_time=request.POST.get('end_time')
            end_time=end_time.split(':')
            hours=int(end_time[0])
            minutes=int(end_time[1])
            end_time=time(hours,minutes)
            delta = timedelta(hours=end_time.hour, minutes=end_time.minute) - timedelta(hours=my_time.hour, minutes=my_time.minute)
            hours, seconds = divmod(delta.total_seconds(), 3600)
            minutes= seconds // 60
            duration= time(int(hours), int(minutes))
            club_name=get_club_name(username)
            club_name=club_name[0][0]
            if is_slot_free(my_date,my_time,duration) :
                obj=Events(name=name,club_name=club_name,date=my_date,time=my_time,duration=duration,endtime=end_time,venue=venue,status=status)
                obj.save()
                messages.success(request,"Event Added Successfully")
            else :
                messages.warning(request,"Time  Slot Already Occupied")
        return render(request,'addevents.html',{'category':category})

def clubtimeline(request):
    if request.user.is_authenticated:
        username=request.user.username
        with connection.cursor() as cursor:
                select_query=f"SELECT CLUB_TYPE,CATEGORY FROM home_clubidentifier where username = '{username}'"
                cursor.execute(select_query)
                result = cursor.fetchall()
                if result:
                    category=result[0][1]
        update_status_of_events()
        rows=[]
        club_name=get_club_name(username)
        club_name=club_name[0][0]
        rows=get_all_completed_events(club_name)
        return render(request,'clubtimeline.html',{'rows' : rows,'category':category})


def dashboard(request):
    rows=[]
    faculty=[]
    events=[]
    if request.user.is_anonymous:
        return redirect("/index.html")
    if request.user.is_authenticated:
        username=request.user.username
        with connection.cursor() as cursor:
                select_query=f"SELECT CLUB_TYPE,CATEGORY FROM home_clubidentifier where username = '{username}'"
                cursor.execute(select_query)
                result = cursor.fetchall()
                if result:
                    category=result[0][1]
        username = request.user.username
        club_name=get_club_name(username)
        club_name=club_name[0][0]
        
        rows=get_all_coordinators(club_name)
        faculty=get_faculty_name(club_name)
        events=get_all_completed_events(club_name)
        events=events[0]
        return render(request,'dashboard.html',{'rows' : rows,'faculty' : faculty,'events' : events,"category":category})

'''def approveRequestOd(request,request_id):
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
        return'''

def approvalStatus(request):
    print("inside approval status")
    if request.user.is_anonymous:
        return redirect("/")
    if request.user.is_authenticated:
        username=request.user.username
        with connection.cursor() as cursor:
                select_query=f"SELECT CLUB_TYPE,CATEGORY FROM home_clubidentifier where username = '{username}'"
                cursor.execute(select_query)
                result = cursor.fetchall()
                if result:
                    type=result[0][0]
                    category=result[0][1]
                    try:
                        if request.method=="POST":
                            roll_no = request.POST.get('roll_no')
                            date = request.POST.get('date')
                            course_code = request.POST.get('course-code')
                            faculty = request.POST.get('faculty')
                            if category=="C":
                                on_duty_approval_status = OnDutyRequest.objects.filter(student_roll_no=roll_no, date_of_od=date, course_code=course_code, faculty_name=faculty, type_of_club=type, username=username)
                            elif category=="SC" or category=="FI":
                                on_duty_approval_status = OnDutyRequest.objects.filter(student_roll_no=roll_no, date_of_od=date, course_code=course_code, faculty_name=faculty, type_of_club=type)

                        else:
                            if category=="C":
                                print("inside C")
                                on_duty_approval_status = OnDutyRequest.objects.filter(type_of_club=type,username=username)
                                # if on_duty_approval_status.exists():
                                #     print("not empty")
                                # else:
                                #     print("emtpy")
                            elif category=="SC" or category=="FI":
                                on_duty_approval_status = OnDutyRequest.objects.filter(type_of_club=type)
                    except OnDutyRequest.DoesNotExist:
                        on_duty_approval_status = None
                    return render(request, "approval_status.html", {'on_duty_approval_status': on_duty_approval_status,'category':category})


def approve(request,request_id=None):
    if request.user.is_anonymous:
        return redirect("/")
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
                    try:
                        if request.method=="POST":
                            if category=="SC":
                                od_object = OnDutyRequest.objects.get(id=request_id)
                                od_object.status="PFI"
                                od_object.save()
                                # approveRequestOd(request,request_id)
                                on_duty_requests = OnDutyRequest.objects.filter(type_of_club=type,status="PSC")
                                # if type=="cultural":
                                #     on_duty_requests = OnDutyRequestClubSports.objects.all()   
                                # elif type=="technical":
                                #     on_duty_requests = OnDutyRequestClubTechnical.objects.all()  
                                # elif type=="sports":
                                #     on_duty_requests = OnDutyRequestClubSports.objects.all() 
                            elif category=="FI":
                                od_object = OnDutyRequest.objects.get(id=request_id)
                                od_object.status="AP"
                                od_object.save()
                                on_duty_requests = OnDutyRequest.objects.filter(type_of_club=type,status="PFI")
                                # approveRequestOd(request,request_id)
                                # if type=="cultural":
                                #     on_duty_requests = OnDutyRequestSCCultural.objects.all()
                                # elif type=="technical":
                                #     on_duty_requests = OnDutyRequestSCTechnical.objects.all()
                                # elif type=="sports":
                                #     on_duty_requests = OnDutyRequestSCCultural.objects.all()
                            return render(request, "approval.html", {'on_duty_requests': on_duty_requests,'category':category})
                        # elif category=="SC" and type=="cultural":
                        #     #display request list of cultural from clubs
                        #     # print("inside sc and cultural")
                        #     # on_duty_requests = OnDutyRequestClubCultural.objects.get()
                        #     on_duty_requests = OnDutyRequest.objects.get(type_of_club=type,status="PSC")
                        # elif category=="SC" and type=="technical":
                        #     #display request list of technical from clubs
                        #     on_duty_requests = OnDutyRequestClubTechnical.objects.all()
                        # elif category=="SC" and type=="sports":
                        #     #display request list of sports from clubs
                        #     on_duty_requests = OnDutyRequestClubSports.objects.all()
                        # elif category=="FI" and type=="cultural":
                        #     #display request list of sports from sc
                        #     on_duty_requests = OnDutyRequestSCCultural.objects.all()
                        # elif category=="FI" and type=="technical":
                        #     #display request list of sports from sc
                        #     on_duty_requests = OnDutyRequestSCTechnical.objects.all()
                        # elif category=="FI" and type=="sports":
                        #     #display request list of sports from sc
                        #     on_duty_requests = OnDutyRequestSCCultural.objects.all()
                        

                        elif category=="SC":
                            on_duty_requests = OnDutyRequest.objects.filter(type_of_club=type,status="PSC")
                        elif category=="FI":
                            on_duty_requests = OnDutyRequest.objects.filter(type_of_club=type,status="PFI")
                    except OnDutyRequest.DoesNotExist:
                        on_duty_requests = None
                    return render(request, "approval.html", {'on_duty_requests': on_duty_requests,'category':category})


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def requestOnDuty(request):
    if request.user.is_anonymous:
        return redirect("/")
    if request.user.is_authenticated:
        username = request.user.username
        with connection.cursor() as cursor:
            select_query=f"SELECT CLUB_TYPE,CATEGORY FROM home_clubidentifier where username = '{username}'"
            cursor.execute(select_query)
            result = cursor.fetchall()
            if result:
                type=result[0][0]
                category=result[0][1]
            if request.method == 'POST':
                username = request.user.username
                roll_nos = request.POST.getlist('roll_no')
                dates = request.POST.getlist('date')
                course_codes = request.POST.getlist('course-code')
                faculties = request.POST.getlist('faculty')
                reasons = request.POST.getlist('reason')            
                if category=="C":
                    if type=="cultural":
                        for i in range(len(roll_nos)):
                            record = OnDutyRequest(
                            student_roll_no=roll_nos[i],
                            date_of_od=dates[i],
                            course_code=course_codes[i],
                            faculty_name=faculties[i],
                            reason=reasons[i],
                            type_of_club="cultural",
                            status="PSC",
                            username=username
                            )
                            record.save()
                        return redirect('/requestOd')
                    elif type=="sports":
                        for i in range(len(roll_nos)):
                            record = OnDutyRequest(
                            student_roll_no=roll_nos[i],
                            date_of_od=dates[i],
                            course_code=course_codes[i],
                            faculty_name=faculties[i],
                            reason=reasons[i],
                            type_of_club="sports",
                            status="PSC",
                            username=username
                            )
                            record.save()
                        return redirect('/requestOd')
                    elif type=="technical":
                        for i in range(len(roll_nos)):
                            record = OnDutyRequest(
                            student_roll_no=roll_nos[i],
                            date_of_od=dates[i],
                            course_code=course_codes[i],
                            faculty_name=faculties[i],
                            reason=reasons[i],
                            type_of_club="technical",
                            status="PSC",
                            username=username
                            )
                            record.save()
                        return redirect('/requestOd')
                elif category=="SC":
                    if type=="cultural":
                        for i in range(len(roll_nos)):
                            record = OnDutyRequest(
                            student_roll_no=roll_nos[i],
                            date_of_od=dates[i],
                            course_code=course_codes[i],
                            faculty_name=faculties[i],
                            reason=reasons[i],
                            type_of_club="cultural",
                            status="PFI",
                            username=username
                            )
                            record.save()
                        return redirect('/requestOd')
                    elif type=="technical":
                        for i in range(len(roll_nos)):
                            record = OnDutyRequest(
                            student_roll_no=roll_nos[i],
                            date_of_od=dates[i],
                            course_code=course_codes[i],
                            faculty_name=faculties[i],
                            reason=reasons[i],
                            type_of_club="technical",
                            status="PFI",
                            username=username
                            )
                            record.save()
                        return redirect('/requestOd')
                    elif type=="sports":
                        for i in range(len(roll_nos)):
                            record = OnDutyRequest(
                            student_roll_no=roll_nos[i],
                            date_of_od=dates[i],
                            course_code=course_codes[i],
                            faculty_name=faculties[i],
                            reason=reasons[i],
                            type_of_club="sports",
                            status="PFI",
                            username=username
                            )
                            record.save()
                        return redirect('/requestOd')                 
        return render(request,"requestOd.html",{'category':category})
    
    

def changePassword(request):
    if request.user.is_anonymous:
        return redirect("/")
    if request.user.is_authenticated:
        if request.method == 'POST':
            current_password = request.POST['current_password']
            new_password = request.POST['new_password']
            confirm_password = request.POST['confirm_new_password']
            user = request.user
            # Check if the current password is correct
            if user.check_password(current_password):
                if new_password == confirm_password:
                    # Change the user's password
                    user.set_password(new_password)
                    user.save()
                    print("changed password")
                    logout(request)
                    return render(request,'index.html')  

        return render(request, 'changePassword.html')


def addUser(request):
    if request.user.is_anonymous:
        return redirect("/")
    if request.user.is_authenticated:
        with connection.cursor() as cursor:
            select_query=f"SELECT CLUB_TYPE,CATEGORY FROM home_clubidentifier where username = '{username}'"
            cursor.execute(select_query)
            result = cursor.fetchall()
            if result:
                type=result[0][0]
                category=result[0][1]
                if category=="FI":
                    if request.method == 'POST':
                        username = request.POST['username']
                        password = request.POST['password']
                        confirm_password = request.POST['confirm_password']
                        if password == confirm_password:
                            # Check if a user with the same username or email already exists
                            if not User.objects.filter(username=username).exists():
                                User.objects.create_user(username=username,password=password)
                            return redirect('adduser.html',{"category":category})
                    return render(request, 'adduser.html',{"category":category})
        return render(request, 'adduser.html')
def profile(request):
    if request.user.is_anonymous:
        return redirect("/")
    if request.user.is_authenticated:
        return render(request,'profile.html')
