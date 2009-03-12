from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    # (r'^home/', include('home.foo.urls')),
    (r'^.*$', 'website.views.index'),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    #(r'^admin/(.*)', admin.site.root),
)

publicidade = patterns('',
	url(r'/cabelo/.*', 'dummy', name='br.cristianaarcangeli.cabelo'),
	url(r'/corpo/.*', 'dummy', name='br.cristianaarcangeli.corpo'),
	url(r'/cris-circula/.*', 'dummy', name='br.cristianaarcangeli.galerias'),
	url(r'/rosto/.*', 'dummy', name='br.cristianaarcangeli.rosto'),
	url(r'/[a-z]*/.*', 'dummy', name='br.cristianaarcangeli.internas'),
	url(r'/$', 'dummy', name='br.cristianaarcangeli.home'),
)