from django.contrib import admin
from django.urls import path, include

from employee.views import *


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('employee.urls')),
    path('api/v1/', include('poll.api_urls')),
]

