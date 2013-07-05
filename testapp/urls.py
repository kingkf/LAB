from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

from django.http import HttpResponse
def hello(request):
    return HttpResponse('hello, world')

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'testapp.views.home', name='home'),
    # url(r'^testapp/', include('testapp.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    url(r'^$', hello),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^webapp/', include('webapp.urls')),
    url(r'^fun/', include('fun.urls')),
)
