from django.urls import path, include

urlpatterns = [
    path('v1/authentication/', include('authentication.urls')),
    path('v1/chucknorris/', include('chucknorris.urls')),
]
