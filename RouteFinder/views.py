# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic

# Create your views here.


class IndexView(generic.TemplateView):
    def index(self):
        return HttpResponse("Hello, world.  You are at the Routefinder index.")
