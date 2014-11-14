from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
   url(r'^$', 'produto.views.index'),
   url(r'^validar/$', 'produto.views.validar'),
   url(r'^validar/$', 'produto.views.validar'),

)
