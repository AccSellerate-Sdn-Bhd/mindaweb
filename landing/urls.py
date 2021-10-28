from django.contrib import admin
from django.urls import path

from django.views.decorators.cache import cache_page

from .views import LandingPageView

app_name= "landing"

urlpatterns = [

    path('', LandingPageView.as_view(), name='landing' ),
]
