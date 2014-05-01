from django.conf.urls import patterns, include, url
from .views import ExtraDataView, UserDetailView

urlpatterns = patterns('',
	url(r'^log-out/$' , 'apps.users.views.LogOut', name='logout'),
	url(r'^extra-data/$' , ExtraDataView.as_view(), name='extra_data'),
	url(r'^usuario/(?P<slug>[-\w]+)/$', UserDetailView.as_view(), name='user_detail'),
)				
