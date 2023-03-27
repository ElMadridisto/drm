from django.contrib import admin

# Register your models here.
from .models import *

@admin.register(Senser)
class SenserAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']
    list_filter =['description']

@admin.register(Measerement)
class MeaserementAdmin(admin.ModelAdmin):
    list_display = ['temperature', 'date_and_time', 'senser']
