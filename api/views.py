from rest_framework import generics
from . import serializers
from django.contrib.auth.models import User
from .models import Station, Interval, Carrier, Carriage, Route


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer


class StationList(generics.ListAPIView):
    queryset = Station.objects.all()
    serializer_class = serializers.StationSerializer


class CarrierList(generics.ListAPIView):
    queryset = Carrier.objects.all()
    serializer_class = serializers.CarrierSerializer


class CarriageList(generics.ListAPIView):
    queryset = Carriage.objects.all()
    serializer_class = serializers.CarriageSerializer


class RouteList(generics.ListAPIView):
    queryset = Route.objects.all()
    serializer_class = serializers.RouteSerializer
