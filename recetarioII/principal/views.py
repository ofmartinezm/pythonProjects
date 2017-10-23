from django.shortcuts import render

# Create your views here.
from django.shortcuts import HttpResponse, render_to_response

#
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import (CreateView, UpdateView, DeleteView)
from django.core.urlresolvers import reverse_lazy
#

from .models  import Bebida

#def lista_bebidas(request):
#	bebidas= Bebida.objects.all()
	#esta no va##bebidas_lista='Hola mundo' #"- ".join(bebidas)
#	return render(request, 'bebidas_list.html',{'bebida':bebidas})

class lista_bebidas(ListView):
	template_name = "bebidas_list.html"
	model=Bebida

class BebidaCreation(CreateView):
    template_name = "tarea_form.html"
    model = Bebida
    success_url = reverse_lazy('lista:lista') 
    fields = ['nombre', 'ingredientes', 'preparacion']	
	

class BebidaDetalle(DetailView):
    template_name = "tarea_detalle.html"
    model = Bebida	


