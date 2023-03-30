from rest_framework import serializers, fields

from .models import Senser, Measerement


class SenserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Senser
        fields = ['id','name', 'description']

class MeaserementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Measerement
        fields = ['temperature', 'date_and_time', 'senser']



class SensorDetailSerializer(serializers.ModelSerializer):
    measurements = MeaserementSerializer(read_only=True, many = True)
    class Meta:
        model = Senser
        fields = ['id', 'name', 'description', 'measurements']