from django.conf.urls import patterns, include, url
from django.conf import settings

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'SistemaDiscusiones.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^' , include('apps.home.urls')), 
    url(r'^' , include('apps.users.urls', namespace='users')),  
    url(r'^' , include('apps.discuss.urls' , namespace='discuss')),
    
    # PYTHON SOCIAL AUTH
    url('', include('social.apps.django_app.urls', namespace='social')),

    #url(r'^static/(?P<path>.*)$', 'django.views.static.serve',{'document_root': settings.STATIC_ROOT}),
    
    url(r'^admin/', include(admin.site.urls)),
)
