from django.contrib import admin
from home.models import *

# Register your models here.
admin.site.register(Contact)
models_list=[RequestOnDuty,Events,ClubList,music,dance,finearts,yoga,ebsb,literaryanddebating,media,photography,netsec,webdev,competitivecoding,iot,robotics,circopt,science,volleyball,cricket,badminton,tabletennis,basketball,carrom,chess,kabbadi,athleticstrack,athleticsfield,football,throwball,ClubIdentifier]
admin.site.register(models_list)

models_list2=[OnDutyRequestSCCultural,OnDutyRequestSCTechnical,OnDutyRequestSCSports,OnDutyRequestClubCultural,OnDutyRequestClubTechnical,OnDutyRequestClubSports]
admin.site.register(models_list2)

admin.site.register(OnDutyRequest)