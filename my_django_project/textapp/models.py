from django.db import models
from django.forms import ModelForm

class SomeText(models.Model):
	name = models.CharField(max_length=100)
	email = models.EmailField(max_length=100)
	username = models.CharField(max_length=100)
	password = models.CharField(max_length=100)

	def __str__(self):
		return self.some_text
