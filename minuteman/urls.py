from django.conf.urls.defaults import patterns, include, url
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^dashboard/$', 'minuteman.views.dashboard', name='dashboard'),
    url(r'^project_summary/$', 'minuteman.views.project_summary', name='project_summary'),
    url(r'^project_total/$', 'minuteman.views.project_total', name='total'),
    url(r'^login/$', 'django.contrib.auth.views.login', {'template_name': 'minuteman/login.html'}),
    url(r'^start/$', 'minuteman.views.start'),
    url(r'^stop/$', 'minuteman.views.stop'),
    url(r'^logout/$', 'django.contrib.auth.views.logout_then_login'),
#    url(r'^register/$', 'minuteman.views.register'),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^send_invoice/', 'minuteman.views.send_invoice'),
)
