from django.db import models,connection
from django import forms
from .models import *
# makemigrations - create changes and store in a file 
# migrate - apply the pending changes created by makemigrations

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=122)
    email = models.CharField(max_length=122)
    phone = models.CharField(max_length=12)
    desc = models.TextField()
    date = models.DateField()

    def __str__(self):
        return self.name

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

class Events(models.Model) :
    name=models.CharField(max_length=122)
    club_name=models.CharField(max_length=122)
    date=models.DateField()
    time=models.TimeField()
    venue=models.CharField(max_length=122)
    status=models.CharField(max_length=122)
    def _str_(self):
        return self.name

    @staticmethod
    def get_all_Departments():
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM home_Events")
            rows=cursor.fetchall()
        return rows

class ClubList(models.Model) :
    name=models.CharField(max_length=122)
    faculty_coordinator=models.CharField(max_length=122)
    category=models.CharField(max_length=122)
    def _str_(self):
        return self.name

    @staticmethod
    def get_all_Departments():
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM home_ClubList")
            rows=cursor.fetchall()
        return rows

class MusicClub(models.Model) :
    roll=models.IntegerField()
    name=models.CharField(max_length=122)
    joining_year=models.IntegerField()
    designation=models.CharField(max_length=122)
    branch=models.CharField(max_length=122)
    def _str_(self):
        return self.name

    @staticmethod
    def get_alifl_Departments():
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM home_MusicClub")
            rows=cursor.fetchall()
        return rows
    
class DanceClub(models.Model) :
    roll=models.IntegerField()
    name=models.CharField(max_length=122)
    joining_year=models.IntegerField()
    designation=models.CharField(max_length=122)
    branch=models.CharField(max_length=122)
    def _str_(self):
        return self.name

    @staticmethod
    def get_all_Departments():
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM home_DanceClub")
            rows=cursor.fetchall()
        return rows
    
class FineartsClub(models.Model) :
    roll=models.IntegerField()
    name=models.CharField(max_length=122)
    joining_year=models.IntegerField()
    designation=models.CharField(max_length=122)
    branch=models.CharField(max_length=122)
    def _str_(self):
        return self.name

    @staticmethod
    def get_all_Departments():
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM home_FineartsClub")
            rows=cursor.fetchall()
        return rows

class YogaClub(models.Model) :
    roll=models.IntegerField()
    name=models.CharField(max_length=122)
    joining_year=models.IntegerField()
    designation=models.CharField(max_length=122)
    branch=models.CharField(max_length=122)
    def _str_(self):
        return self.name

    @staticmethod
    def get_all_Departments():
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM home_YogaClub")
            rows=cursor.fetchall()
        return rows
    
class EBSBClub(models.Model) :
    roll=models.IntegerField()
    name=models.CharField(max_length=122)
    joining_year=models.IntegerField()
    designation=models.CharField(max_length=122)
    branch=models.CharField(max_length=122)
    def _str_(self):
        return self.name

    @staticmethod
    def get_all_Departments():
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM home_EBSBClub")
            rows=cursor.fetchall()
        return rows
    
class LiteraryandDebatingClub(models.Model) :
    roll=models.IntegerField()
    name=models.CharField(max_length=122)
    joining_year=models.IntegerField()
    designation=models.CharField(max_length=122)
    branch=models.CharField(max_length=122)
    def _str_(self):
        return self.name

    @staticmethod
    def get_all_Departments():
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM home_LiteraryandDebatingClub")
            rows=cursor.fetchall()
        return rows

class MediaClub(models.Model) :
    roll=models.IntegerField()
    name=models.CharField(max_length=122)
    joining_year=models.IntegerField()
    designation=models.CharField(max_length=122)
    branch=models.CharField(max_length=122)
    def _str_(self):
        return self.name

    @staticmethod
    def get_all_Departments():
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM home_MediaClub")
            rows=cursor.fetchall()
        return rows
    
class PhotographyClub(models.Model) :
    roll=models.IntegerField()
    name=models.CharField(max_length=122)
    joining_year=models.IntegerField()
    designation=models.CharField(max_length=122)
    branch=models.CharField(max_length=122)
    def _str_(self):
        return self.name

    @staticmethod
    def get_all_Departments():
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM home_PhotographyClub")
            rows=cursor.fetchall()
        return rows
    
class NetsecClub(models.Model) :
    roll=models.IntegerField()
    name=models.CharField(max_length=122)
    joining_year=models.IntegerField()
    designation=models.CharField(max_length=122)
    branch=models.CharField(max_length=122)
    def _str_(self):
        return self.name

    @staticmethod
    def get_all_Departments():
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM home_NetsecClub")
            rows=cursor.fetchall()
        return rows
    

class WebDevClub(models.Model) :
    roll=models.IntegerField()
    name=models.CharField(max_length=122)
    joining_year=models.IntegerField()
    designation=models.CharField(max_length=122)
    branch=models.CharField(max_length=122)
    def _str_(self):
        return self.name

    @staticmethod
    def get_all_Departments():
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM home_WebDevClub")
            rows=cursor.fetchall()
        return rows

class CompetitiveCodingClub(models.Model) :
    roll=models.IntegerField()
    name=models.CharField(max_length=122)
    joining_year=models.IntegerField()
    designation=models.CharField(max_length=122)
    branch=models.CharField(max_length=122)
    def _str_(self):
        return self.name

    @staticmethod
    def get_all_Departments():
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM home_CompetitiveCodingClub")
            rows=cursor.fetchall()
        return rows
    
class IOTClub(models.Model) :
    roll=models.IntegerField()
    name=models.CharField(max_length=122)
    joining_year=models.IntegerField()
    designation=models.CharField(max_length=122)
    branch=models.CharField(max_length=122)
    def _str_(self):
        return self.name

    @staticmethod
    def get_all_Departments():
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM home_IOTClub")
            rows=cursor.fetchall()
        return rows

class RoboticsClub(models.Model) :
    roll=models.IntegerField()
    name=models.CharField(max_length=122)
    joining_year=models.IntegerField()
    designation=models.CharField(max_length=122)
    branch=models.CharField(max_length=122)
    def _str_(self):
        return self.name

    @staticmethod
    def get_all_Departments():
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM home_RoboticsClub")
            rows=cursor.fetchall()
        return rows
    
class CircoptClub(models.Model) :
    roll=models.IntegerField()
    name=models.CharField(max_length=122)
    joining_year=models.IntegerField()
    designation=models.CharField(max_length=122)
    branch=models.CharField(max_length=122)
    def _str_(self):
        return self.name

    @staticmethod
    def get_all_Departments():
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM home_CircoptClub")
            rows=cursor.fetchall()
        return rows
    
class ScienceClub(models.Model) :
    roll=models.IntegerField()
    name=models.CharField(max_length=122)
    joining_year=models.IntegerField()
    designation=models.CharField(max_length=122)
    branch=models.CharField(max_length=122)
    def _str_(self):
        return self.name

    @staticmethod
    def get_all_Departments():
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM home_ScienceClub")
            rows=cursor.fetchall()
        return rows

class VolleyBallClub(models.Model) :
    roll=models.IntegerField()
    name=models.CharField(max_length=122)
    joining_year=models.IntegerField()
    designation=models.CharField(max_length=122)
    branch=models.CharField(max_length=122)
    def _str_(self):
        return self.name

    @staticmethod
    def get_all_Departments():
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM home_VolleyBallClub")
            rows=cursor.fetchall()
        return rows
    
class CricketClub(models.Model) :
    roll=models.IntegerField()
    name=models.CharField(max_length=122)
    joining_year=models.IntegerField()
    designation=models.CharField(max_length=122)
    branch=models.CharField(max_length=122)
    def _str_(self):
        return self.name

    @staticmethod
    def get_all_Departments():
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM home_CricketClub")
            rows=cursor.fetchall()
        return rows

class BadmintonClub(models.Model) :
    roll=models.IntegerField()
    name=models.CharField(max_length=122)
    joining_year=models.IntegerField()
    designation=models.CharField(max_length=122)
    branch=models.CharField(max_length=122)
    def _str_(self):
        return self.name

    @staticmethod
    def get_all_Departments():
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM home_BadmintonClub")
            rows=cursor.fetchall()
        return rows
    
class TableTennisClub(models.Model) :
    roll=models.IntegerField()
    name=models.CharField(max_length=122)
    joining_year=models.IntegerField()
    designation=models.CharField(max_length=122)
    branch=models.CharField(max_length=122)
    def _str_(self):
        return self.name

    @staticmethod
    def get_all_Departments():
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM home_TableTennisClub")
            rows=cursor.fetchall()
        return rows

class BasketBallClub(models.Model) :
    roll=models.IntegerField()
    name=models.CharField(max_length=122)
    joining_year=models.IntegerField()
    designation=models.CharField(max_length=122)
    branch=models.CharField(max_length=122)
    def _str_(self):
        return self.name

    @staticmethod
    def get_all_Departments():
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM home_BasketBallClub")
            rows=cursor.fetchall()
        return rows

class CarromClub(models.Model) :
    roll=models.IntegerField()
    name=models.CharField(max_length=122)
    joining_year=models.IntegerField()
    designation=models.CharField(max_length=122)
    branch=models.CharField(max_length=122)
    def _str_(self):
        return self.name

    @staticmethod
    def get_all_Departments():
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM home_CarromClub")
            rows=cursor.fetchall()
        return rows
    
class ChessClub(models.Model) :
    roll=models.IntegerField()
    name=models.CharField(max_length=122)
    joining_year=models.IntegerField()
    designation=models.CharField(max_length=122)
    branch=models.CharField(max_length=122)
    def _str_(self):
        return self.name

    @staticmethod
    def get_all_Departments():
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM home_ChessClub")
            rows=cursor.fetchall()
        return rows
    
class KabbadiClub(models.Model) :
    roll=models.IntegerField()
    name=models.CharField(max_length=122)
    joining_year=models.IntegerField()
    designation=models.CharField(max_length=122)
    branch=models.CharField(max_length=122)
    def _str_(self):
        return self.name

    @staticmethod
    def get_all_Departments():
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM home_KabbadiClub")
            rows=cursor.fetchall()
        return rows

class AthleticsTrackClub(models.Model) :
    roll=models.IntegerField()
    name=models.CharField(max_length=122)
    joining_year=models.IntegerField()
    designation=models.CharField(max_length=122)
    branch=models.CharField(max_length=122)
    def _str_(self):
        return self.name

    @staticmethod
    def get_all_Departments():
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM home_AthleticsTrackClub")
            rows=cursor.fetchall()
        return rows

class AthleticsFieldClub(models.Model) :
    roll=models.IntegerField()
    name=models.CharField(max_length=122)
    joining_year=models.IntegerField()
    designation=models.CharField(max_length=122)
    branch=models.CharField(max_length=122)
    def _str_(self):
        return self.name

    @staticmethod
    def get_all_Departments():
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM home_AthleticsFieldClub")
            rows=cursor.fetchall()
        return rows

class FootBallClub(models.Model) :
    roll=models.IntegerField()
    name=models.CharField(max_length=122)
    joining_year=models.IntegerField()
    designation=models.CharField(max_length=122)
    branch=models.CharField(max_length=122)
    def _str_(self):
        return self.name

    @staticmethod
    def get_all_Departments():
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM home_FootBallClub")
            rows=cursor.fetchall()
        return rows
    
class ThrowBallClub(models.Model) :
    roll=models.IntegerField()
    name=models.CharField(max_length=122)
    joining_year=models.IntegerField()
    designation=models.CharField(max_length=122)
    branch=models.CharField(max_length=122)
    def _str_(self):
        return self.name

    @staticmethod
    def get_all_Departments():
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM home_ThrowBallClub")
            rows=cursor.fetchall()
        return rows

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

