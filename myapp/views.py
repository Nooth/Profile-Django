# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, render_to_response

def index(request):
	return render_to_response('index.html')

def projects(request):
	return render_to_response('projects.html')

# Create your views here.
