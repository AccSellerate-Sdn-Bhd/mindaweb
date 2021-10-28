from django.shortcuts import render, redirect, reverse
from django.views.generic import TemplateView


# Create your views here.
class LandingPageView(TemplateView):
    template_name='landing/landing.html'
