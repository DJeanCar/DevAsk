#encoding:utf-8
from django import forms
from .models import Question
from apps.users.models import User


class CreateQuestionForm(forms.ModelForm):

	title = forms.CharField(widget = forms.TextInput(attrs={
					'class' : 'form-control',
					'placeholder' : 'título'
		}))

	description = forms.CharField(widget = forms.Textarea(attrs={
					'class' : 'form-control',
					'placeholder' : 'contenido',
					'rows' : 4
		}))

	class Meta:
		model = Question