from django.conf.urls.defaults import patterns, include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^dashboard/$', 'minuteman.views.dashboard'),
    url(r'^project_summary/$', 'minuteman.views.project_list' ),
    url(r'^login/$', 'django.contrib.auth.views.login', {'template_name': 'minuteman/login.html'}),
    url(r'^logout/$', 'django.contrib.auth.views.logout_then_login'),
#    url(r'^register/$', 'minuteman.views.register'),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
