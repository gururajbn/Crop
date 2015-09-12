from django import forms
from .models import videos

class videoform(forms.ModelForm):
	class Meta:
		model = videos
		fields= ['x','y','width','height']