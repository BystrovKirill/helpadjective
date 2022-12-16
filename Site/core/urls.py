from django.urls import path
from .views import *

app_name = 'core'

urlpatterns = [
    # Registration Urls
    path('registration/invalid/', InvalidRegistrationView.as_view(), name='register-invalid'),
    path('registration/volunteer/', VolunteerRegistrationView.as_view(), name='register-volunteer'),
    path('invalidlist/', InvalidAPIList.as_view(), name='invalid-list'),
    path('volunteerlist/', VolunteerAPIList.as_view(), name='volunteer-list'),
    path('helprequestlist/', HelpRequestList.as_view()),
    path('userlist/', UsersList.as_view()),
    #path('invalidlist/<int:pk>/', InvalidAPIList.as_view()),
    #path('volunteerlist/<int:pk>/', VolunteerAPIList.as_view()),
    path('helprequestlist/<int:pk>/', HelpRequestDetail.as_view()),
]