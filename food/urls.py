from django.urls import path
from food.views import *
app_name='foodies'

urlpatterns = [
    path('sweet/',sweet,name='sweet'),
]
