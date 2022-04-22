from django import forms
from .models import Maqola

class Maqolaqosh(forms.ModelForm):
	class Meta:
		model = Maqola
		fields = ['title','context']