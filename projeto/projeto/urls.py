from django.conf.urls import patterns, include, url

urlpatterns = patterns('produto.views',
                       url(r'^$', 'index'),
                       url(r'^cadastro/$', 'cadastro'),
                       url(r'^validar/$', 'validar'),
                       
                       url(r'^i18n/', include('django.conf.urls.i18n')),
)
