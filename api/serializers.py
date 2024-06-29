from rest_framework import serializers 

from empapp.models import Employee,profile


class EmployeeSerializer(serializers.ModelSerializer):

    class Meta:

        model=Employee

        fields="__all__"


class ProfileSerializer(serializers.ModelSerializer):

    class Meta:

        model=profile

        fields="__all__"