from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.views.generic import View,DetailView
from django.core.mail import EmailMessage

from .forms import ExtraDataForm
from .models import User
from apps.discuss.models import Question

class ExtraDataView(View):

	def get(self, request, *args, **kwargs):
		form = ExtraDataForm()
		if request.user.status:
			return redirect('/')
		else:		
			return render(request, 'users/extra_data.html', {'form':form})

	def post(self, request, *args, **kwargs):
		form = ExtraDataForm(request.POST)
		if form.is_valid():
			request.user.username = request.POST['username']
			request.user.email = request.POST['email']
			request.user.status = True
			request.user.save()
			send_email(request)
			return redirect('/')
		else:
			error_username = form['username'].errors.as_text()
			error_email = form['email'].errors.as_text()
			ctx = {'error_username':error_username, 'error_email':error_email}
			return render(request, 'users/extra_data.html', ctx)		

def LogOut(request):
	logout(request)
	return redirect('/')


def send_email(request):

	msg = EmailMessage(subject='Bienvenida',
						from_email = 'DevCode.la <devcodela@gmail.com',
						to = [request.user.email])

	msg.template_name = 'welcome'
	msg.template_content = {

		'std_content00' : '<h1>Hola %s Bienvenido a DevAsk</h1>' % request.user
	}

	msg.send()


class UserDetailView(DetailView):

	model = User
	context_object_name = 'user'
	slug_field = 'username'

	def get_context_data(self, **kwargs):
		context = super(UserDetailView, self).get_context_data(**kwargs)
		questions = Question.objects.filter(user = context['object']).order_by('created')
		tags = [ question.tag.all() for question in questions ]
		context['ques_tags'] = zip(questions , tags)

		facebook = context['object'].social_auth.filter(provider='facebook')
		if facebook:
			context['facebook'] = facebook[0].extra_data['id']

		twitter = context['object'].social_auth.filter(provider='twitter')
		if twitter:
			context['twitter'] = twitter[0].extra_data['access_token']['screen_name']
		return context