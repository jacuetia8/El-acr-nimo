from django.conf.urls import patterns, include, url
import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'Lgm.views.home', name='home'),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^',include('lgm.apps.home.urls')),
    url(r'^media/(?P<path>.*)$','django.views.static.serve',{'document_root':settings.MEDIA_ROOT}),
    #url(r'^',include('Lgm.apps.reportes.urls')),
    # url(r'^Lgm/', include('Lgm.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:

    # Uncomment the next line to enable the admin:
)
