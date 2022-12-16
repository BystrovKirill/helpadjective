from rest_framework import serializers
from rest_auth.registration.serializers import RegisterSerializer
from rest_framework.authtoken.models import Token
from .models import *


class InvalidCustomRegistrationSerializer(RegisterSerializer):
    invalid = serializers.PrimaryKeyRelatedField(read_only=True, )  # by default allow_null = False
    category_inv = serializers.CharField(required=True)
    limit_inv = serializers.CharField(required=True)
    fio = serializers.CharField(required=True)


    def get_cleaned_data(self):
        data = super(InvalidCustomRegistrationSerializer, self).get_cleaned_data()
        extra_data = {
            'category_inv': self.validated_data.get('category_inv', ''),
            'limit_inv': self.validated_data.get('limit_inv', ''),
            'fio': self.validated_data.get('fio', ''),
        }
        data.update(extra_data)
        return data

    def save(self, request):
        user = super(InvalidCustomRegistrationSerializer, self).save(request)
        user.is_invalid = True
        user.save()
        invalid = Invalid(invalid=user, category_inv=self.cleaned_data.get('category_inv'),
                          limit_inv=self.cleaned_data.get('limit_inv'),
                          fio=self.cleaned_data.get('fio'))
        invalid.save()
        return user


class VolunteerCustomRegistrationSerializer(RegisterSerializer):
    volunteer = serializers.PrimaryKeyRelatedField(read_only=True, )  # by default allow_null = False
    organization_ident = serializers.CharField(required=True)
    # is_helping = serializers.BooleanField(required=True)
    fio = serializers.CharField(required=True)

    def get_cleaned_data(self):
        data = super(VolunteerCustomRegistrationSerializer, self).get_cleaned_data()
        extra_data = {
            'organization_ident': self.validated_data.get('organization_ident', ''),
            # 'is_helping': self.validated_data.get('is_helping', ''),
            'fio': self.validated_data.get('fio', ''),
        }
        data.update(extra_data)
        return data

    def save(self, request):
        user = super(VolunteerCustomRegistrationSerializer, self).save(request)
        user.is_volunteer = True
        user.save()
        volunteer = Volunteer(volunteer=user, organization_ident=self.cleaned_data.get('organization_ident'),
                              # is_helping=self.cleaned_data.get('is_helping'),
                              fio=self.cleaned_data.get('fio'))
        volunteer.save()
        return user


class InvalidSerializer(serializers.ModelSerializer):
    #helprequest = serializers.PrimaryKeyRelatedField(many=False, read_only=True)

    class Meta:
        model = Invalid
        depth = 1
        fields = '__all__'


class VolunteerSerializer(serializers.ModelSerializer):
    #helprequest = serializers.PrimaryKeyRelatedField(many=False, read_only=True)

    class Meta:
        model = Volunteer
        depth = 1
        fields = '__all__'
        fields = '__all__'


class HelpRequestSerializer(serializers.ModelSerializer):
    #owner = serializers.ReadOnlyField(source='owner.fio')
    #helper = serializers.ReadOnlyField(source='helper.fio', required=False)

    class Meta:
        model = HelpRequest
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    #helprequest = serializers.PrimaryKeyRelatedField(many=False, read_only=True)

    class Meta:
        model = User
        fields = ("id", "is_superuser", "username", "email", "date_joined", "is_invalid", "is_volunteer")