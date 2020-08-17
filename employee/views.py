from django.shortcuts import render
from rest_framework import viewsets
from .serializers import EmployeeSerializer




class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = EmployeeSerializer
    pass
# Create your views here.
