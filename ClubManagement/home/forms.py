# from django import forms 
# from django.forms import modelformset_factory
# from .models import *

# class DutyRequestFormClubCultural(forms.ModelForm):
#     class Meta:
#         model = OnDutyRequestClubCultural
#         fields = ['student_roll_no', 'date_of_od','course_code','faculty_name','reason']

# class DutyRequestFormClubTehnical(forms.ModelForm):
#     class Meta:
#         model = OnDutyRequestClubTechnical
#         fields = ['student_roll_no', 'date_of_od','course_code','faculty_name','reason']

# class DutyRequestFormClubSports(forms.ModelForm):
#     class Meta:
#         model = OnDutyRequestClubSports
#         fields = ['student_roll_no', 'date_of_od','course_code','faculty_name','reason']


# class DutyRequestFormSCCultural(forms.ModelForm):
#     class Meta:
#         model = OnDutyRequestSCCultural
#         fields = ['student_roll_no', 'date_of_od','course_code','faculty_name','reason']

# class DutyRequestFormSCTechnical(forms.ModelForm):
#     class Meta:
#         model = OnDutyRequestSCTechnical
#         fields = ['student_roll_no', 'date_of_od','course_code','faculty_name','reason']

# class DutyRequestFormSCSports(forms.ModelForm):
#     class Meta:
#         model = OnDutyRequestSCSports
#         fields = ['student_roll_no', 'date_of_od','course_code','faculty_name','reason']

# class ApprovalFormClubCultural(forms.ModelForm):
#     class Meta:
#         model = OnDutyRequestClubCultural
#         fields = []
# class ApprovalFormSCCultural(forms.ModelForm):
#     class Meta:
#         model = OnDutyRequestSCCultural
#         fields = []
# class ApprovalFormClubTechnical(forms.ModelForm):
#     class Meta:
#         model = OnDutyRequestClubTechnical
#         fields = []
# class ApprovalFormSCTechnical(forms.ModelForm):
#     class Meta:
#         model = OnDutyRequestSCTechnical
#         fields = []
# class ApprovalFormClubSports(forms.ModelForm):
#     class Meta:
#         model = OnDutyRequestClubSports
#         fields = []
# class ApprovalFormSCSports(forms.ModelForm):
#     class Meta:
#         model = OnDutyRequestSCSports
#         fields = []

# # DutyRequestFormSetClubCultural = modelformset_factory(
# #     OnDutyRequestClubCultural, form=DutyRequestFormClubCultural, extra=1
# # )
# # DutyRequestFormSetClubTehnical = modelformset_factory(
# #     OnDutyRequestClubTechnical, form=DutyRequestFormClubTehnical, extra=1
# # )
# # DutyRequestFormSetClubSports = modelformset_factory(
# #     OnDutyRequestClubSports, form=DutyRequestFormClubSports, extra=1
# # )
# # DutyRequestFormSetSCCultural = modelformset_factory(
# #     OnDutyRequestSCCultural, form = DutyRequestFormSCTechnical, extra=1
# # )
# # DutyRequestFormSetSCSports = modelformset_factory(
# #     OnDutyRequestSCSports, form = DutyRequestFormSCSports, extra=1
# # )
# # DutyRequestFormSetSCTechnical = modelformset_factory(
# #     OnDutyRequestSCTechnical, form = DutyRequestFormSCTechnical, extra=1
# # )