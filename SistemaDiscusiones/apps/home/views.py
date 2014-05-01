from django.shortcuts import render
from django.views.generic import ListView

from apps.discuss.models import Question
from apps.users.models import User

class IndexView(ListView):
	template_name = 'home/index.html'
	queryset = Question.objects.all()[:5]

	def get_queryset(self):
		tags = [ question.tag.all() for question in self.queryset]
		return zip(self.queryset, tags)

	def get_context_data(self, **kwargs):
		context = super(IndexView, self).get_context_data(**kwargs)
		context['total_questions'] = Question.objects.count()
		context['total_users'] = User.objects.exclude(is_superuser=True).count()
		return context