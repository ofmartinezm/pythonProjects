from django.conf.urls import url
from django.contrib import admin
from .views import  lista_bebidas, BebidaCreation,BebidaDetalle

urlpatterns = [
	#url(r'^lista/',views.lista_bebidas),
	url(r'^$', lista_bebidas.as_view(), name='lista'),
	url(r'^nuevo$', BebidaCreation.as_view(), name='nuevo'),
	# con el formato se indica que se va a enviar un dato numerico y de tipo primary key
	url(r'^(?P<pk>\d+)$', BebidaDetalle.as_view(), name='detalle'),
	#url(r'^detalle/(?P<nombre>[-\w\s]+)$', BebidaDetalle.as_view(), name='detalle'),
	# con el formato (?P<nombre>[-\w\s]+)$ se indica que se va a enviar el parametro nombre de tipo string que admite espacios en blanco


]
