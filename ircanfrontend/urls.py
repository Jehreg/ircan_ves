from django.conf.urls.defaults import *

urlpatterns = patterns('ircanfrontend.views',
     (r'^$','index'),
     (r'^reboot/(?P<veid>\d+)/(?P<hostid>\d+)$','reboot'),
     (r'^start/(?P<veid>\d+)/(?P<hostid>\d+)$','start'),
     (r'^stop/(?P<veid>\d+)/(?P<hostid>\d+)$','stop'),
)
