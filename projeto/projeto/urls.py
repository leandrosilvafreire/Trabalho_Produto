from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
   url(r'^$', 'produto.views.cadastro'),
   url(r'^validar/$', 'produto.views.validar'),
   
)
