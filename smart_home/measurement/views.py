# TODO: опишите необходимые обработчики, рекомендуется использовать generics APIView классы:
# TODO: ListCreateAPIView, RetrieveUpdateAPIView, CreateAPIView
from django.shortcuts import  render
from rest_framework.decorators import APIView
from rest_framework.response import Response
from rest_framework.generics import RetrieveAPIView
from rest_framework import generics, status
from .models import Senser, Measerement
from .serializers import SenserSerializer, MeaserementSerializer, SensorDetailSerializer


class SenserView(APIView):
    def get(self, request):
        sensor = Senser.objects.all()
        sen = SenserSerializer(sensor, many=True)
        return Response(sen.data)

class MeaserementView(APIView):
    def get(self, request):
        measerement = Measerement.objects.all()
        mea = MeaserementSerializer(measerement, many=True)
        return Response(mea.data)

class SenserDetailView(RetrieveAPIView):
    queryset = Senser.objects.all()
    serializer_class = SensorDetailSerializer