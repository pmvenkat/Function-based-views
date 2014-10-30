from django.shortcuts import render
from django.http import HttpResponse


def http_response(request):
	return HttpResponse("This is a simple response !")