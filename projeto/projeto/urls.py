from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
   
   url(r'^$', 'produto.views.index'),
   url(r'^cadastro/$', 'produto.views.cadastro'),
   url(r'^validar/$', 'produto.views.validar'),
   
   
                       
   url(r'^i18n/', include('django.conf.urls.i18n')),
                       
   
)
