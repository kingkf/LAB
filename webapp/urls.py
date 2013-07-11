from django.conf.urls import patterns, url

from webapp import views

urlpatterns = patterns('',
    url(r'^$', views.current_datetime, name='current_datetime'),     
    url(r'^search-form/$', views.search_form),
    url(r'^search/$', views.search),
    url(r'^register/$', views.register_page),
    url(r'^login/$',  views.login_user), 
    url(r'^product/([0-9]+)/$', views.show_product),
    url(r'^index/$', views.square),
    url(r'^index/([12])/$', views.square),
)
