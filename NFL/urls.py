from django.urls import path
from .views import *

urlpatterns = [
path('', home, name='home'),
path('nfl/offense/', offense, name='offense'),
path('nfl/defense/', defense, name='defense'),
]