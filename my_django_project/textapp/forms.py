from django import forms
from .models import SomeText

class SomeTextForm(forms.ModelForm):
	class Meta:
		model = SomeText
		fields = [
			'name',
			'email',
			'username',
			'password'
		]	
		widgets = {
			'password' : forms.PasswordInput()
		}
