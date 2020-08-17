from django.urls import path
from rest_framework import routers



from employee.views import *


routes = routers.DefaultRouter()

routers.register('employee', EmployeeViewSet)

urlpatterns = [
    path('employee', include(router.urls)),
]