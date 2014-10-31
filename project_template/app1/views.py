from django.shortcuts import render
from django.http import HttpResponse

from django.contrib.auth.models import User

import json


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


def json_response(request):
    users = User.objects.all()
    res = {
        'users': {}
    }
    for user in users:
        res['users'][user.username] = {
            'id': user.id,
            'first_name': user.first_name,
            'last_name': user.last_name,
            'username': user.username
        }

    json_res = json.dumps(res)
    return HttpResponse(json_res, mimetype="application/json")


