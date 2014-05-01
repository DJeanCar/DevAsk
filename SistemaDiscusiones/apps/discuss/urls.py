from django.conf.urls import patterns, include, url
from .views import QuestionListView, QuestionCreateView, QuestionDetailView
from django.views.decorators.cache import cache_page

urlpatterns = patterns('',
	url(r'^preguntas/$' , QuestionListView.as_view(), name='questions'),
	url(r'^preguntar/$', QuestionCreateView.as_view(), name='create_question'),
	url(r'^pregunta/(?P<slug>[-\w]+)/$' , 
			QuestionDetailView.as_view(), name = 'detail_question'),
	url(r'^buscar-ajax/$' , 'apps.discuss.views.BuscarAjax' , name='buscar'),
)
