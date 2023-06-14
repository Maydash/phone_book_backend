from rest_framework import serializers
from .models import *


class PlaceOfWorkSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlaceOfWork
        fields = '__all__'


class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location
        fields = '__all__'


class DepartmentNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = DepartmentName
        fields = '__all__'


class PositionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Position
        fields = '__all__'


class PhoneBookSerializer(serializers.ModelSerializer):
    class Meta:
        model = PhoneBook
        fields = '__all__'
