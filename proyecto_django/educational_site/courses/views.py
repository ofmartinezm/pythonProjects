from django.shortcuts import render
from django.http import HttpResponse

from .models import Course

# Create your views here.

def courses(request):
	curso= Course.objects.all()
	"""course_list="- ".join([str(course) for course in curso])
	return HttpResponse(course_list)"""
	return render(request, 'courses/course_list.html',{'courses':curso})