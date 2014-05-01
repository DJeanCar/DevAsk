from django import forms
from .models import User

class ExtraDataForm(forms.ModelForm):
	username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-input'}))

	class Meta:
		model = User
		fields = ('username' , 'email')

