from django.db import models

# Create your models here.

class Maqola(models.Model):
	title = models.CharField(max_length=250)
	context = models.TextField(blank=True)
	photo = models.ImageField(upload_to='photos/%Y/%m/%d/')
	
	def __str__(self):
		return self.title

