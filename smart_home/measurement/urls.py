from django.urls import path

from .views import SenserView, MeaserementView, SenserDetailView


urlpatterns = [
    path('sensors/', SenserView.as_view()),
    path('measurements/', MeaserementView.as_view()),
    path('sensors/<pk>', SenserDetailView.as_view()),

]
