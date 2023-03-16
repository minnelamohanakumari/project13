from django.urls import path
from banana.views import *
app_name='something'
urlpatterns=[
    path('banana/',banana,name='banana'),
]