 from django.conf.urls import patterns, include, url

 urlpatterns = patterns('app1.views',
     url(r'^http_response/$', 'http_response', name='http_response'),
     url(r'^simple_template/$', 'simple_template', name='simple_template'),
 )
