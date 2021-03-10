from django import forms
from django.forms import ModelForm
from .models import contactForm

class contact(forms.ModelForm):
	class Meta:
		model= contactForm
		fields={
			'name',
			'email',
			'query',
			'mobile_number',
			'message',
			

		}
		widgets = {'message': forms.Textarea(attrs={'row': 2, 'col': 2,'placeholder':'Please write something...'}),
        }	
		
