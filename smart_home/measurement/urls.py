from django.urls import path

from .views import SenserView, MeaserementView, SenserDetailView


urlpatterns = [
    path('sensors/', SenserView.as_view()),
    path('measurement/', MeaserementView.as_view()),
    path('sensors/<pk>', SenserDetailView.as_view()),

]
