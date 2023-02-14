from unicodedata import name
from django.urls import path, include 

from homeapp.views import * 

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    # path('', inputuserinfo(), name='home'),
    # path('', HomeCreateView.as_view(), name='home')
]