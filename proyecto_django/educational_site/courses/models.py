from django.db import models

# Create your models here.


class Course(models.Model):
	create_at=models.DateTimeField(auto_now_add=True)
	name=models.CharField(max_length=180)
	description=models.TextField()
	def __str__(self):
		return self.name
	
	
	