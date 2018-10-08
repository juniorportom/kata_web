from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^editar/(?P<idTrabajador>\d+)$', views.editar_perfil, name='editar'),
    url(r'^register', views.register, name='register'),
    url(r'^detail', views.detalle_trabajador, name='detail'),
    url(r'^trabajador/(?P<pk>\d+)$', views.detail),
    url(r'^addComment', views.add_comment),
    url(r'^mostrarComentarios/(?P<idTrabajador>\d+)$', views.mostrarComentarios),
    url(r'^mostrarTrabajadores/(?P<tipo>\w+)$', views.mostrarTrabajadores),
    url(r'^mostrarTrabajadores', views.mostrarTrabajadores),
    url(r'^login$', views.login),
    url(r'^logout$', views.logout),
]
