from django.urls import path

from .views import *

urlpatterns = [
    path('poll', PollAPIView.as_view()),
    path('poll/<int:id>', PollDetailAPIView.as_view()) 
]