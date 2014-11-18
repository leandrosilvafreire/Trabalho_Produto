from django.conf.urls import patterns, include, url

<<<<<<< HEAD
urlpatterns = patterns('',
   
   url(r'^$', 'produto.views.index'),
   url(r'^cadastro/$', 'produto.views.cadastro'),
   url(r'^validar/$', 'produto.views.validar'),
   
   
=======
urlpatterns = patterns('produto.views',
                       url(r'^$', 'index'),
                       url(r'^cadastro/$', 'cadastro'),
                       url(r'^validar/$', 'validar'),
>>>>>>> b3bce85639d1dd43fa17fd0dbb238676a51d75b5
                       
                       url(r'^i18n/', include('django.conf.urls.i18n')),
)
