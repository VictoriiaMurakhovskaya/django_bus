from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Station, Interval, Carrier, Carriage, Route


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username']


class StationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Station
        fields = ['id', 'name']


class CarrierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Carrier
        fields = ['id', 'name']


class IntervalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Interval
        fields = ['id', 'start_time', 'start', 'finish_time', 'finish', 'cost']


class RouteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Route
        fields = ['id', 'carrier', 'start', 'finish']


class CarriageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Carriage
        fields = ['id', 'date', 'route', 'tickets']

