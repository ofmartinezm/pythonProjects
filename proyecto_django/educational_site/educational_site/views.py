from django.http import HttpResponse
from django.shortcuts import render


def hello_world(request):
	"""return HttpResponse('Hola Django')"""
	return render(request,'home.html')
	
	