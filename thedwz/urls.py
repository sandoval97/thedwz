
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from thedwz import api

urlpatterns = [
    path('api/', include(api)),
    path('admin/', admin.site.urls),
]