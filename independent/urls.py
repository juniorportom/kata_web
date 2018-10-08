from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^register', views.register, name='register'),
    url(r'^detail', views.detalle_trabajador, name='detail'),
    url(r'^trabajador/(?P<pk>\d+)$', views.detail),
    url(r'^mostrarTrabajadores/(?P<tipo>\w+)$', views.mostrarTrabajadores),
    url(r'^mostrarTrabajadores', views.mostrarTrabajadores),
]
