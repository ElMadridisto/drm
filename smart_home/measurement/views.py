# TODO: опишите необходимые обработчики, рекомендуется использовать generics APIView классы:
# TODO: ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView
from django.shortcuts import  render
from rest_framework.decorators import APIView
from rest_framework.response import Response
from rest_framework.generics import RetrieveAPIView, ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView
from rest_framework import generics, status
from .models import Senser, Measerement
from .serializers import SenserSerializer, MeaserementSerializer, SensorDetailSerializer


class SenserView(ListCreateAPIView):
    queryset = Senser.objects.all()
    serializer_class = SenserSerializer


class MeaserementView(CreateAPIView):
    queryset = Measerement.objects.all()
    serializer_class = MeaserementSerializer


class SenserDetailView(RetrieveUpdateAPIView):
    queryset = Senser.objects.all()
    serializer_class = SensorDetailSerializer