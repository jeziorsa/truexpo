from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'truexpo.views.home', name='home'),
    # url(r'^truexpo/', include('truexpo.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^p/$', 'app.views.index'),
    url(r'^p/(?P<project_id>\d+)/$', 'app.views.detail'),
    url(r'^admin/', include(admin.site.urls)),
)
