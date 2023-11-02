from django.db import models,connection
from django import forms
from .models import *
from datetime import timedelta
from datetime import time
from datetime import date, datetime
# makemigrations - create changes and store in a file 
# migrate - apply the pending changes created by makemigrations


def get_all_coordinators(club_name) :
       with connection.cursor() as cursor:
        query="SELECT name FROM home_{} WHERE designation='coordinator' ORDER BY joining_year".format(club_name)
        cursor.execute(query)
        rows = cursor.fetchall()
        return rows

def get_faculty_name(club_name) :
    with connection.cursor() as cursor:
        query="select faculty_coordinator from home_ClubList where club_name=%s"
        cursor.execute(query,[club_name])
        rows=cursor.fetchall()
        return rows[0][0]


def is_slot_free(my_date, my_time, my_duration):
    with connection.cursor() as cursor:
        cursor.execute("SELECT time, duration from home_Events where date=%s", [my_date])
        rows = cursor.fetchall()
    my_datetime = datetime.combine(my_date, my_time)
    for row in rows:
        event_start_time = datetime.combine(my_date, row[0])
        event_duration = row[1]
        event_end_time = event_start_time + timedelta(hours=event_duration.hour, minutes=event_duration.minute, seconds=event_duration.second)

        if not (my_datetime >= event_end_time or my_datetime + timedelta(hours=my_duration.hour, minutes=my_duration.minute, seconds=my_duration.second) <= event_start_time) and my_datetime != event_end_time:
            return False

    return True



def update_status_of_events():
    current_date = date.today()
    current_time = datetime.now().time()
    events_to_update = Events.objects.filter(date__lte=current_date, endtime__lte=current_time,status='upcoming')
    events_to_update.update(status="completed")



def delete_event(name) :
    event_to_delete = Events.objects.get(name=name)
    event_to_delete.delete()

def delete_member(club_name,roll) :
    query="delete from home_{} where roll=%d".format(club_name)
    with connection.cursor() as cursor:
        cursor.execute(query,[roll])


def get_all_contacts():
        rows=[]
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM home_Contact")
            rows = cursor.fetchall()
        return rows[:5][:]
        
def get_club_name(user) :
    query="SELECT club_name from home_ClubIdentifier where username=%s"
    with connection.cursor() as cursor:
        cursor.execute(query,[user])
        club_name=cursor.fetchall()
    return club_name

def get_club_details() :
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM home_ClubList")
        rows = cursor.fetchall()
        return rows

def myfunc(e) :
    return e[3]

def get_all_member(club_name) :
    query="SELECT * FROM home_{}".format(club_name)
    rows=[]
    current_year = datetime.now().year
    with connection.cursor() as cursor:
        cursor.execute(query)
        rows=cursor.fetchall()
    co_ordinators=[]
    members=[]
    for i in rows :
        if "coordinator" in i :
            co_ordinators.append(list(i))
        else :
            members.append(list(i))
    co_ordinators.sort(key=myfunc)
    members.sort(key=myfunc)
    co_ordinators.extend(members)
    new_rows=[]
    for i in co_ordinators :
        temp=[]
        temp.append(i[1])
        temp.append(i[2])
        temp.append(i[5].upper())
        if(current_year+1-i[3]==1) :
            temp.append(str(current_year+1-i[3])+"st Year")
        if(current_year+1-i[3]==2) :
            temp.append(str(current_year+1-i[3])+"nd Year")
        if(current_year+1-i[3]==3) :
            temp.append(str(current_year+1-i[3])+"rd Year")
        if(current_year+1-i[3]==4) :
            temp.append(str(current_year+1-i[3])+"th Year")
        string=i[4].capitalize()
        temp.append(string)
        new_rows.append(temp)
    print(new_rows)
    objs=[]
    for i in range(len(new_rows)) :
        print(new_rows[i][0])
        roll=new_rows[i][0]
        name=new_rows[i][1]
        branch=new_rows[i][2]
        joining_year=new_rows[i][3]
        designation=new_rows[i][4]
        obj=Members(name,roll,branch,joining_year,designation)
        objs.append(obj)
    return objs
    

class Members() :
    def __init__(self,name,roll,branch,joining_year,designation) :
        self.name=name
        self.roll=roll
        self.branch=branch
        self.joining_year=joining_year
        self.designation=designation


def upcomming_events(club_name) :
    today = date.today()
    events = Events.objects.filter(status='upcoming', date__gte=today,club_name=club_name).order_by('date', 'time')
    print(events)
    return events



#********************************don't remove this*********************************************

def get_all_events(club_name) :
    query="select * from home_Events where club_name=%s order by date,time"
    with connection.cursor() as cursor:
        cursor.execute(query,[club_name])
        rows=cursor.fetchall()
    return rows[:5][1:]


    




def get_all_completed_events(club_name) :
    query="select * from home_Events where club_name=%s and status='completed' order by date,time"
    with connection.cursor() as cursor:
        cursor.execute(query,[club_name])
        rows=cursor.fetchall()
    new_rows=[]
    for i in rows :
        temp=[]
        temp.append(i[1])
        temp.append(i[3])
        new_rows.append(temp)
    temp=new_rows[:5]
    temp=temp[::-1]
    return temp














# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=122)
    email = models.CharField(max_length=122)
    phone = models.CharField(max_length=12)
    desc = models.TextField()
    date = models.DateField()

    def __str__(self):
        return self.name
class ClubIdentifier(models.Model):
    username=models.CharField(max_length=122,primary_key=True)
    club_name=models.CharField(max_length=122)
    choices=[
        ("cultural","cultural"),
        ("technical","technical"),
        ("sports","sports")
    ]
    club_type=models.CharField(max_length=122,choices=choices,default="sports")
    choices=[
        ("FI","Faculty Incharge"),
        ("SC","Student Council"),
        ("C","Club")
    ]
    category=models.CharField(max_length=122,choices=choices)

    @staticmethod
    def get_all_users():
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM home_clubidentifier")
            records=cursor.fetchall()
        return records

class RequestOnDuty(models.Model) :
    roll=models.IntegerField()
    club_name=models.CharField(max_length=122)
    date=models.DateField()
    course_code=models.CharField(max_length=122)
    faculty=models.CharField(max_length=122)
    def _str_(self):
        return self.club_name

    @staticmethod
    def get_all_Departments():
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM home_RequestOnDuty")
            rows=cursor.fetchall()
        return rows


# class OnDutyRequestSC(models.Model):
#     student_roll_no=models.CharField(max_length=6)
#     date_of_od=models.DateField()
#     course_code=models.CharField(max_length=7)
#     faculty_name=models.TextField(max_length=1000)
#     reason=models.CharField(max_length=122)
#     choices=[
#         ("cultural","cultural"),
#         ("technical","technical"),
#         ("sports","sports")
#     ]
#     type_of_club=models.CharField(max_length=122,choices=choices)

class OnDutyRequest(models.Model):
    student_roll_no=models.CharField(max_length=6)
    date_of_od=models.DateField()
    course_code=models.CharField(max_length=7)
    faculty_name=models.CharField(max_length=122)
    reason=models.TextField(max_length=200)
    choices=[
        ("cultural","cultural"),
        ("technical","technical"),
        ("sports","sports")
    ]
    type_of_club=models.CharField(max_length=122,choices=choices)
    choices_of_status=[
        ("PSC","Pending at SC level"),
        ("PFI","Pending at FI level"),
        ("AP","Approved by faculty incharge")
    ]
    status=models.CharField(max_length=3,choices=choices_of_status,default="PSC")
    username=models.CharField(max_length=122,default="user@user")


# class OnDutyRequestFacultyIncharge(models.Model):
#     student_roll_no=models.CharField(max_length=6)
#     date_of_od=models.DateField()
#     course_code=models.CharField(max_length=7)
#     faculty_name=models.TextField(max_length=1000)
#     reason=models.CharField(max_length=122)
#     choices=[
#         ("cultural","cultural"),
#         ("technical","technical"),
#         ("sports","sports")
#     ]
#     type_of_club=models.CharField(max_length=122,choices=choices)

class OnDutyRequestSCCultural(models.Model):
    student_roll_no=models.CharField(max_length=6)
    date_of_od=models.DateField()
    course_code=models.CharField(max_length=7)
    faculty_name=models.TextField(max_length=1000)
    reason=models.CharField(max_length=122)
    # choices=[
    #     ("cultural","cultural"),
    #     ("technical","technical"),
    #     ("sports","sports")
    # ]
    # type_of_club=models.CharField(max_length=122,choices=choices)
class OnDutyRequestSCTechnical(models.Model):
    student_roll_no=models.CharField(max_length=6)
    date_of_od=models.DateField()
    course_code=models.CharField(max_length=7)
    faculty_name=models.TextField(max_length=1000)
    reason=models.CharField(max_length=122)
    # choices=[
    #     ("cultural","cultural"),
    #     ("technical","technical"),
    #     ("sports","sports")
    # ]
    # type_of_club=models.CharField(max_length=122,choices=choices)
class OnDutyRequestSCSports(models.Model):
    student_roll_no=models.CharField(max_length=6)
    date_of_od=models.DateField()
    course_code=models.CharField(max_length=7)
    faculty_name=models.TextField(max_length=1000)
    reason=models.CharField(max_length=122)
    # choices=[
    #     ("cultural","cultural"),
    #     ("technical","technical"),
    #     ("sports","sports")
    # ]
    # type_of_club=models.CharField(max_length=122,choices=choices)

class OnDutyRequestClubCultural(models.Model):
    student_roll_no=models.CharField(max_length=6)
    date_of_od=models.DateField()
    course_code=models.CharField(max_length=7)
    faculty_name=models.CharField(max_length=122)
    reason=models.CharField(max_length=122)
    # choices=[
    #     ("cultural","cultural"),
    #     ("technical","technical"),
    #     ("sports","sports")
    # ]
    # type_of_club=models.CharField(max_length=122,choices=choices)
class OnDutyRequestClubTechnical(models.Model):
    student_roll_no=models.CharField(max_length=6)
    date_of_od=models.DateField()
    course_code=models.CharField(max_length=7)
    faculty_name=models.CharField(max_length=122)
    reason=models.CharField(max_length=122)
    # choices=[
    #     ("cultural","cultural"),
    #     ("technical","technical"),
    #     ("sports","sports")
    # ]
    # type_of_club=models.CharField(max_length=122,choices=choices)
class OnDutyRequestClubSports(models.Model):
    student_roll_no=models.CharField(max_length=6)
    date_of_od=models.DateField()
    course_code=models.CharField(max_length=7)
    faculty_name=models.CharField(max_length=122)
    reason=models.CharField(max_length=122)
    # choices=[
    #     ("cultural","cultural"),
    #     ("technical","technical"),
    #     ("sports","sports")
    # ]
    # type_of_club=models.CharField(max_length=122,choices=choices)


class Events(models.Model) :
    name=models.CharField(max_length=122)
    club_name=models.CharField(max_length=122)
    date=models.DateField()
    time=models.TimeField()
    duration=models.TimeField(default='01:00:00')
    endtime=models.TimeField(default='01:00:00')
    venue=models.CharField(max_length=122)
    status=models.CharField(max_length=122)
    def __str__(self):
        return self.name

    @staticmethod
    def get_all_events():
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM home_Events")
            rows=cursor.fetchall()
        dict_rows = {} 
        for i in range(len(rows)) :
            dict_rows[i]=rows[i]
        return dict_rows

class ClubList(models.Model) :
    club_name=models.CharField(max_length=122)
    faculty_coordinator=models.CharField(max_length=122)
    category=models.CharField(max_length=122)
    def __str__(self):
        return self.club_name

    @staticmethod
    def get_all_clubs():
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM home_ClubList")
            rows=cursor.fetchall()
        dict_rows = {} 
        for i in range(len(rows)) :
            dict_rows[i]=rows[i]
        return dict_rows

class music(models.Model) :
    roll=models.IntegerField()
    name=models.CharField(max_length=122)
    joining_year=models.IntegerField()
    designation=models.CharField(max_length=122)
    branch=models.CharField(max_length=122)
    def __str__(self):
        return self.name


    
class dance(models.Model) :
    roll=models.IntegerField()
    name=models.CharField(max_length=122)
    joining_year=models.IntegerField()
    designation=models.CharField(max_length=122)
    branch=models.CharField(max_length=122)
    def __str__(self):
        return self.name


    
class finearts(models.Model) :
    roll=models.IntegerField()
    name=models.CharField(max_length=122)
    joining_year=models.IntegerField()
    designation=models.CharField(max_length=122)
    branch=models.CharField(max_length=122)
    def __str__(self):
        return self.name


          

class yoga(models.Model) :
    roll=models.IntegerField()
    name=models.CharField(max_length=122)
    joining_year=models.IntegerField()
    designation=models.CharField(max_length=122)
    branch=models.CharField(max_length=122)
    def __str__(self):
        return self.name


   

    
class ebsb(models.Model) :
    roll=models.IntegerField()
    name=models.CharField(max_length=122)
    joining_year=models.IntegerField()
    designation=models.CharField(max_length=122)
    branch=models.CharField(max_length=122)
    def __str__(self):
        return self.name


          

    
class literaryanddebating(models.Model) :
    roll=models.IntegerField()
    name=models.CharField(max_length=122)
    joining_year=models.IntegerField()
    designation=models.CharField(max_length=122)
    branch=models.CharField(max_length=122)
    def __str__(self):
        return self.name


         


class media(models.Model) :
    roll=models.IntegerField()
    name=models.CharField(max_length=122)
    joining_year=models.IntegerField()
    designation=models.CharField(max_length=122)
    branch=models.CharField(max_length=122)
    def __str__(self):
        return self.name

class photography(models.Model) :
    roll=models.IntegerField()
    name=models.CharField(max_length=122)
    joining_year=models.IntegerField()
    designation=models.CharField(max_length=122)
    branch=models.CharField(max_length=122)
    def __str__(self):
        return self.name


    
class netsec(models.Model) :
    roll=models.IntegerField()
    name=models.CharField(max_length=122)
    joining_year=models.IntegerField()
    designation=models.CharField(max_length=122)
    branch=models.CharField(max_length=122)
    def __str__(self):
        return self.name



class webdev(models.Model) :
    roll=models.IntegerField()
    name=models.CharField(max_length=122)
    joining_year=models.IntegerField()
    designation=models.CharField(max_length=122)
    branch=models.CharField(max_length=122)
    def __str__(self):
        return self.name


        

class competitivecoding(models.Model) :
    roll=models.IntegerField()
    name=models.CharField(max_length=122)
    joining_year=models.IntegerField()
    designation=models.CharField(max_length=122)
    branch=models.CharField(max_length=122)
    def __str__(self):
        return self.name


       

    
class iot(models.Model) :
    roll=models.IntegerField()
    name=models.CharField(max_length=122)
    joining_year=models.IntegerField()
    designation=models.CharField(max_length=122)
    branch=models.CharField(max_length=122)
    def __str__(self):
        return self.name


 


class robotics(models.Model) :
    roll=models.IntegerField()
    name=models.CharField(max_length=122)
    joining_year=models.IntegerField()
    designation=models.CharField(max_length=122)
    branch=models.CharField(max_length=122)
    def __str__(self):
        return self.name

    
class circopt(models.Model) :
    roll=models.IntegerField()
    name=models.CharField(max_length=122)
    joining_year=models.IntegerField()
    designation=models.CharField(max_length=122)
    branch=models.CharField(max_length=122)
    def __str__(self):
        return self.name

class science(models.Model) :
    roll=models.IntegerField()
    name=models.CharField(max_length=122)
    joining_year=models.IntegerField()
    designation=models.CharField(max_length=122)
    branch=models.CharField(max_length=122)
    def __str__(self):
        return self.name

class volleyball(models.Model) :
    roll=models.IntegerField()
    name=models.CharField(max_length=122)
    joining_year=models.IntegerField()
    designation=models.CharField(max_length=122)
    branch=models.CharField(max_length=122)
    def __str__(self):
        return self.name
 
class cricket(models.Model) :
    roll=models.IntegerField()
    name=models.CharField(max_length=122)
    joining_year=models.IntegerField()
    designation=models.CharField(max_length=122)
    branch=models.CharField(max_length=122)
    def __str__(self):
        return self.name

class badminton(models.Model) :
    roll=models.IntegerField()
    name=models.CharField(max_length=122)
    joining_year=models.IntegerField()
    designation=models.CharField(max_length=122)
    branch=models.CharField(max_length=122)
    def __str__(self):
        return self.name

class tabletennis(models.Model) :
    roll=models.IntegerField()
    name=models.CharField(max_length=122)
    joining_year=models.IntegerField()
    designation=models.CharField(max_length=122)
    branch=models.CharField(max_length=122)
    def __str__(self):
        return self.name

class basketball(models.Model) :
    roll=models.IntegerField()
    name=models.CharField(max_length=122)
    joining_year=models.IntegerField()
    designation=models.CharField(max_length=122)
    branch=models.CharField(max_length=122)
    def __str__(self):
        return self.name


class carrom(models.Model) :
    roll=models.IntegerField()
    name=models.CharField(max_length=122)
    joining_year=models.IntegerField()
    designation=models.CharField(max_length=122)
    branch=models.CharField(max_length=122)
    def __str__(self):
        return self.name

class chess(models.Model) :
    roll=models.IntegerField()
    name=models.CharField(max_length=122)
    joining_year=models.IntegerField()
    designation=models.CharField(max_length=122)
    branch=models.CharField(max_length=122)
    def __str__(self):
        return self.name

class kabbadi(models.Model) :
    roll=models.IntegerField()
    name=models.CharField(max_length=122)
    joining_year=models.IntegerField()
    designation=models.CharField(max_length=122)
    branch=models.CharField(max_length=122)
    def __str__(self):
        return self.name


class athleticstrack(models.Model) :
    roll=models.IntegerField()
    name=models.CharField(max_length=122)
    joining_year=models.IntegerField()
    designation=models.CharField(max_length=122)
    branch=models.CharField(max_length=122)
    def __str__(self):
        return self.name

class athleticsfield(models.Model) :
    roll=models.IntegerField()
    name=models.CharField(max_length=122)
    joining_year=models.IntegerField()
    designation=models.CharField(max_length=122)
    branch=models.CharField(max_length=122)
    def __str__(self):
        return self.name


class football(models.Model) :
    roll=models.IntegerField()
    name=models.CharField(max_length=122)
    joining_year=models.IntegerField()
    designation=models.CharField(max_length=122)
    branch=models.CharField(max_length=122)
    def __str__(self):
        return self.name

class throwball(models.Model) :
    roll=models.IntegerField()
    name=models.CharField(max_length=122)
    joining_year=models.IntegerField()
    designation=models.CharField(max_length=122)
    branch=models.CharField(max_length=122)
    def __str__(self):
        return self.name

