from django.shortcuts import render
from rest_auth.registration.views import RegisterView
from rest_framework import generics
from .models import *
from django.db.models import Q
from .serializers import *


class InvalidRegistrationView(RegisterView):
    serializer_class = InvalidCustomRegistrationSerializer


class VolunteerRegistrationView(RegisterView):
    serializer_class = VolunteerCustomRegistrationSerializer


class InvalidAPIList(generics.ListCreateAPIView):
    queryset = Invalid.objects.all()
    serializer_class = InvalidSerializer


class VolunteerAPIList(generics.ListCreateAPIView):
    queryset = Volunteer.objects.all()
    serializer_class = VolunteerSerializer


'''
class InvalidAPIView(generics.UpdateAPIView):
    queryset = Invalid.objects.all()
    serializer_class = InvalidSerializer


class VolunteerAPIView(generics.UpdateAPIView):
    queryset = Volunteer.objects.all()
    serializer_class = VolunteerSerializer
'''


class HelpRequestList(generics.ListCreateAPIView):
    queryset = HelpRequest.objects.filter(helper='')
    serializer_class = HelpRequestSerializer

    # def perform_create(self, serializer):
    #    serializer.save(owner=self.request.user)


class HelpRequestDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = HelpRequest.objects.all()
    serializer_class = HelpRequestSerializer


class UsersList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
