from django.db import models

# Create your models here.
class Bebida(models.Model):
	nombre = models.CharField(max_length=50)
	ingredientes = models.TextField()
	preparacion = models.TextField()
	def __str__(self):
		return self.nombre

"""class Receta(models.Model):
  titulo = models.CharField(max_length=100, unique=True)
  ingredientes = models.TextField(help_text='Redacta los ingredientes')
  prepacion = models.TextField(verbose_name='Preparación')
  imagen = models.ImageField(upload_to='recetas', verbose_name='Imágen')
  tiempo_registro = models.DateTimeField(auto_now=True)
  usuario = models.ForeignKey(User)
	
  def __unicode__(self):
      return self.titulo		"""