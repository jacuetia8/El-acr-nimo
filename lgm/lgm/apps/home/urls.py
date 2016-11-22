from django.conf.urls.defaults import patterns,url


urlpatterns = patterns('lgm.apps.home.views',
		url(r'^$','index_view', name = 'vista_principal'),
		url(r'^add/clase/$','add_clase_view', name = 'vista_agregar_clase'),
		url(r'^login/$', 'login_view', name = 'vista_login'),
		url(r'^registro/$', 'register_view', name = 'vista_registro'),
		url(r'^logout/$', 'logout_view', name = 'vista_logout'),
		url(r'^tanita/$', 'tanita_view', name = 'vista_tanita'),
		url(r'^contact/$', 'contact_view', name = 'vista_contact'),
		
)


