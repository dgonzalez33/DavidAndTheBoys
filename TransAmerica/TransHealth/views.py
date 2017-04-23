# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from django.views.generic import TemplateView
from django.http import HttpResponse
# Create your views here.

class HomeView(TemplateView):
	def get(self, request, **kwargs):
		return render(request, 'index.html', context=None)
	# def post(self, request):
	# 	# do something here with request.body
	# 	print request.body
	# 	return HttpResponse("Done")
@csrf_exempt 
def setInformation(request):
	return HttpResponse(request.body);

class SimulationView(TemplateView):
	template_name = "Simulation.html"