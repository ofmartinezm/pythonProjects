from django.shortcuts import render,render_to_response

from django.template.loader import get_template
from django.template import Context
from django.http import HttpResponse

import datetime

def current_datetime(request):
    now=datetime.datetime.now()
    #t=get_template('current_datetime.html')
    #t = render_to_string('current_datetime.html', ctx)
    #html="<html><body>It is now %s.</body></html>" % now
    #return render(request, 'current_datetime.html',{'current_datetime':now})
    return render_to_response('current_datetime.html', {'current_date': now})

def hours_ahead(request, offset):
    #offset = int(offset)
    dt = datetime.datetime.now() + datetime.timedelta(hours=int(offset))
    #html = "<html><body>In %s hour(s), it will be %s.</body></html>" % (offset, dt)
    return render_to_response('hours_ahead.html', {'next_time': dt})
