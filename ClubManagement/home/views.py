from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,logout,login
from home.models import *
from .forms import *
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
def about(request):
    return render(request,'about.html')
def dashboard(request):
    if request.user.is_authenticated:
        return render(request,'dashboard.html')
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

def approveRequestOd(request,request_id):
    if request.user.is_authenticated:
        username=request.user.username
        with connection.cursor() as cursor:
                select_query=f"SELECT CLUB_TYPE,CATEGORY FROM home_clubidentifier where username = '{username}'"
                cursor.execute(select_query)
                result = cursor.fetchall()
                if result:
                    type,category=result
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

# def approveRequestOdFI(request,request_id):
#     if request.user.is_authenticated:
#         username=request.user.username
#         with connection.cursor() as cursor:
#                 select_query=f"SELECT CLUB_TYPE,CATEGORY FROM home_clubidentifier where username = '{username}'"
#                 cursor.execute(select_query)
#                 result = cursor.fetchall()
#                 if result:
#                     type,category=result
#                     if category=="FI":
#                         duty_request=OnDutyRequestSC.objects.get(id=request_id)
#                         if duty_request:
#                             # on_duty_sc = OnDutyRequest(
#                             # student_roll_no=duty_request.student_roll_no,
#                             # date_of_od=duty_request.date_of_od,
#                             # course_code=duty_request.course_code,
#                             # faculty_name=duty_request.faculty_name,
#                             # reason=duty_request.reason,
#                             # type_of_club=duty_request.type_of_club)
#                             # on_duty_sc.save()
#                             duty_request.delete()
#                             return 
#                 else:
#                     return
#     else:
#         return

def approval(request):
    if request.user.is_authenticated:
        username=request.user.username
        with connection.cursor() as cursor:
                select_query=f"SELECT CLUB_TYPE,CATEGORY FROM home_clubidentifier where username = '{username}'"
                cursor.execute(select_query)
                result = cursor.fetchall()
                if result:
                    type,category=result
                    if request.method=="POST":
                        if category=="SC":
                            approveRequestOd(request,request.id)
                            if type=="cultural":
                                on_duty_requests = OnDutyRequestClubCultural.objects.all()
                                approval_forms = [ApprovalFormClubCultural(instance=request) for request in on_duty_requests]
                                return render(request,"approval.html",{'on_duty_requests': on_duty_requests, 'approval_forms': approval_forms})
                            elif type=="technical":
                                on_duty_requests = OnDutyRequestClubTechnical.objects.all()
                                approval_forms = [ApprovalFormClubTechnical(instance=request) for request in on_duty_requests]
                                return render(request,"approval.html",{'on_duty_requests': on_duty_requests, 'approval_forms': approval_forms})
                            elif type=="sports":
                                on_duty_requests = OnDutyRequestClubSports.objects.all()
                                approval_forms = [ApprovalFormClubSports(instance=request) for request in on_duty_requests]
                                return render(request,"approval.html",{'on_duty_requests': on_duty_requests, 'approval_forms': approval_forms})
                        elif category=="FI":
                            approveRequestOd(request,request.id)
                            if type=="cultural":
                                on_duty_requests = OnDutyRequestSCCultural.objects.all()
                                approval_forms = [ApprovalFormSCCultural(instance=request) for request in on_duty_requests]
                                return render(request,"approval.html",{'on_duty_requests': on_duty_requests, 'approval_forms': approval_forms})
                            elif type=="technical":
                                on_duty_requests = OnDutyRequestSCTechnical.objects.all()
                                approval_forms = [ApprovalFormSCTechnical(instance=request) for request in on_duty_requests]
                                return render(request,"approval.html",{'on_duty_requests': on_duty_requests, 'approval_forms': approval_forms})
                            elif type=="sports":
                                on_duty_requests = OnDutyRequestSCCultural.objects.all()
                                approval_forms = [ApprovalFormSCSports(instance=request) for request in on_duty_requests]
                                return render(request,"approval.html",{'on_duty_requests': on_duty_requests, 'approval_forms': approval_forms})
                    elif category=="SC" and type=="cultural":
                        #display request list of cultural from clubs
                        on_duty_requests = OnDutyRequestClubCultural.objects.all()
                        approval_forms = [ApprovalFormClubCultural(instance=request) for request in on_duty_requests]
                        return render(request,"approval.html",{'on_duty_requests': on_duty_requests, 'approval_forms': approval_forms})
                        
                    elif category=="SC" and type=="technical":
                        #display request list of technical from clubs
                        on_duty_requests = OnDutyRequestClubTechnical.objects.all()
                        approval_forms = [ApprovalFormClubTechnical(instance=request) for request in on_duty_requests]
                        return render(request,"approval.html",{'on_duty_requests': on_duty_requests, 'approval_forms': approval_forms})
                    elif category=="SC" and type=="sports":
                        #display request list of sports from clubs
                        on_duty_requests = OnDutyRequestClubSports.objects.all()
                        approval_forms = [ApprovalFormClubSports(instance=request) for request in on_duty_requests]
                        return render(request,"approval.html",{'on_duty_requests': on_duty_requests, 'approval_forms': approval_forms})
                    elif category=="FI" and type=="cultural":
                        #display request list of sports from sc
                        on_duty_requests = OnDutyRequestSCCultural.objects.all()
                        approval_forms = [ApprovalFormSCCultural(instance=request) for request in on_duty_requests]
                        return render(request,"approval.html",{'on_duty_requests': on_duty_requests, 'approval_forms': approval_forms})
                    elif category=="FI" and type=="technical":
                        #display request list of sports from sc
                        on_duty_requests = OnDutyRequestSCTechnical.objects.all()
                        approval_forms = [ApprovalFormSCTechnical(instance=request) for request in on_duty_requests]
                        return render(request,"approval.html",{'on_duty_requests': on_duty_requests, 'approval_forms': approval_forms})
                    elif category=="FI" and type=="sports":
                        #display request list of sports from sc
                        on_duty_requests = OnDutyRequestSCCultural.objects.all()
                        approval_forms = [ApprovalFormSCSports(instance=request) for request in on_duty_requests]
                        return render(request,"approval.html",{'on_duty_requests': on_duty_requests, 'approval_forms': approval_forms})
                    


def requestOnDuty(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            username=request.user.username
            with connection.cursor() as cursor:
                select_query=f"SELECT CLUB_TYPE,CATEGORY FROM home_clubidentifier where username = '{username}'"
                cursor.execute(select_query)
                result = cursor.fetchall()
                if result:
                    type,category=result
                    if category=="C":
                        if type=="cultural":
                            formset = DutyRequestFormSetClubCultural(request.POST, queryset=OnDutyRequestClubCultural.objects.none())
                            if formset.is_valid():
                                for form in formset:
                                    if form.cleaned_data:
                                        form.save()
                                        # duty_request_club = form.save(commit=False)
                                        #  duty_request_club.type_of_club = type
                                        # duty_request_club.save()
                                return redirect('/requestOd')
                        elif type=="sports":
                            formset = DutyRequestFormSetClubSports(request.POST, queryset=OnDutyRequestClubSports.objects.none())
                            if formset.is_valid():
                                for form in formset:
                                    if form.cleaned_data:
                                        form.save()
                                        # duty_request_club = form.save(commit=False)
                                        #  duty_request_club.type_of_club = type
                                        # duty_request_club.save()
                                return redirect('/requestOd')
                        elif type=="technical":
                            formset = DutyRequestFormSetClubTehnical(request.POST, queryset=OnDutyRequestClubTechnical.objects.none())
                            if formset.is_valid():
                                for form in formset:
                                    if form.cleaned_data:
                                        form.save()
                                        # duty_request_club = form.save(commit=False)
                                        #  duty_request_club.type_of_club = type
                                        # duty_request_club.save()
                                return redirect('/requestOd')
                    elif category=="SC":
                        if type=="cultural":
                            formset = DutyRequestFormSCCultural(request.POST,queryset=OnDutyRequestSCCultural.objects.none())
                            if formset.is_valid():
                                for form in formset:
                                    if form.cleaned_data:
                                        form.save()
                                        # duty_request_sc = form.save(commit=False)
                                        # duty_request_sc.type_of_club = type
                                        # duty_request_sc.save()
                                return redirect('/requestOd')
                        elif type=="technical":
                            formset = DutyRequestFormSCTechnical(request.POST,queryset=OnDutyRequestSCTechnical.objects.none())
                            if formset.is_valid():
                                for form in formset:
                                    if form.cleaned_data:
                                        form.save()
                                        # duty_request_sc = form.save(commit=False)
                                        # duty_request_sc.type_of_club = type
                                        # duty_request_sc.save()
                                return redirect('/requestOd')
                        elif type=="sports":
                            formset = DutyRequestFormSCSports(request.POST,queryset=OnDutyRequestSCSports.objects.none())
                            if formset.is_valid():
                                for form in formset:
                                    if form.cleaned_data:
                                        form.save()
                                        # duty_request_sc = form.save(commit=False)
                                        # duty_request_sc.type_of_club = type
                                        # duty_request_sc.save()
                                return redirect('/requestOd')
            
        else:
            username=request.user.username
            with connection.cursor() as cursor:
                select_query=f"SELECT CLUB_TYPE,CATEGORY FROM home_clubidentifier where username = '{username}'"
                cursor.execute(select_query)
                result = cursor.fetchall()
                if result:
                    type,category=result
                    if category=="C":
                        if type=="cultural":
                            formset = DutyRequestFormSetClubCultural(queryset=OnDutyRequestClubCultural.objects.none())
                        elif type=="technical":
                            formset = DutyRequestFormSetClubTehnical(queryset=OnDutyRequestClubCultural.objects.none())
                        elif type=="sports":
                            formset = DutyRequestFormSetClubSports(queryset=OnDutyRequestClubCultural.objects.none())
                    elif category=="SC":
                        if type=="cultural":
                            formset = DutyRequestFormSCCultural(queryset=OnDutyRequestSCCultural.objects.none())
                        elif type=="technical":
                            formset = DutyRequestFormSCTechnical(queryset=OnDutyRequestSCTechnical.objects.none())
                        elif type=="sports":
                            formset = DutyRequestFormSCSports(queryset=OnDutyRequestSCSports.objects.none())
        return render(request, 'requestOd.html', {'formset': formset})
        #     roll_numbers = request.POST.getlist('roll_number[]')
        #     dates = request.POST.getlist('date[]')
        #     course_codes = request.POST.getlist('course_code[]')
        #     faculties = request.POST.getlist('faculty[]')
        #     reasons = request.POST.getlist('reason[]')
        #     username=request.user.username
        #     with connection.cursor() as cursor:
        #         select_query=f"SELECT CLUB_TYPE,CATEGORY FROM home_clubidentifier where username = '{username}'"
        #         cursor.execute(select_query)
        #         result = cursor.fetchall()
        #         if result:
        #             type,category=result
        #             if category=="SC":
        #                 for i in range(len(roll_numbers)):
        #                     record = OnDutySC(
        #                     roll_number=roll_numbers[i],
        #                     date=dates[i],
        #                     course_code=course_codes[i],
        #                     faculty=faculties[i],
        #                     reason=reasons[i],
        #                     type_of_club=type
        #                     )
        #                     record.save()
        #             elif category=="C":
        #                 for i in range(len(roll_numbers)):
        #                     record = OnDutyClub(
        #                     roll_number=roll_numbers[i],
        #                     date=dates[i],
        #                     course_code=course_codes[i],
        #                     faculty=faculties[i],
        #                     reason=reasons[i],
        #                     type_of_club=type
        #                     )
        #                     record.save()
        # return render(request,'requestOd.html')
                    
                        
            
            
        
