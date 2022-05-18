from django.urls import path
from .api.router import router

app_name = "chucknorris"

urlpatterns = [] + router.urls