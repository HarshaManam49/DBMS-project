from django.contrib import admin
from home.models import *

# Register your models here.
admin.site.register(Contact)
models_list=[RequestOnDuty,Events,ClubList,MusicClub,DanceClub,FineartsClub,YogaClub,EBSBClub,LiteraryandDebatingClub,MediaClub,PhotographyClub,NetsecClub,WebDevClub,CompetitiveCodingClub,IOTClub,RoboticsClub,CircoptClub,ScienceClub,VolleyBallClub,CricketClub,BadmintonClub,TableTennisClub,BasketBallClub,CarromClub,ChessClub,KabbadiClub,AthleticsTrackClub,AthleticsFieldClub,FootBallClub,ThrowBallClub,ClubIdentifier]
admin.site.register(models_list)

models_list2=[OnDutyRequestSCCultural,OnDutyRequestSCTechnical,OnDutyRequestSCSports,OnDutyRequestClubCultural,OnDutyRequestClubTechnical,OnDutyRequestClubSports]
admin.site.register(models_list2)

admin.site.register(OnDutyRequest)