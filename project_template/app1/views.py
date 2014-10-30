from django.shortcuts import render
from django.http import HttpResponse

from django.contrib.auth.models import User


def http_response(request):
	return HttpResponse("This is a simple response !")


def simple_template(request):
	return render(request, "app1/simple_template.html", {})

def users(request):
	users = User.objects.all()
	context = {
		'users': users
	}
	return render(request, "app1/users.html", context)

