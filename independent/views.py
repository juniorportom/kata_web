import datetime

# import boto
from django.conf import settings
from django.contrib.auth.models import User
from django.core import serializers
from django.http import HttpResponseRedirect, HttpResponse
from django.views.decorators.csrf import csrf_exempt

from .models import Trabajador
#Comentario
from .models import TiposDeServicio
from .forms import TrabajadorForm, UserForm
from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.contrib import auth


# Create your views here.
def index(request):
    trabajadores = Trabajador.objects.all()
    tipos_de_servicios = TiposDeServicio.objects.all()
    form_trabajador = TrabajadorForm(request.POST)
    form_usuario = UserForm(request.POST)

    context = {'trabajadores': trabajadores, 'tipos_de_servicios': tipos_de_servicios,
               'form_trabajador': form_trabajador, 'form_usuario': form_usuario, 'base_url': settings.STATIC_URL}

    return render(request, 'independent/index.html', context)


def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = User.objects.create_user(username=username, password=password)
        user.first_name = request.POST.get('nombre')
        user.last_name = request.POST.get('apellidos')
        user.email = request.POST.get('correo')
        user.save()
        image = "";
        if(request.FILES['imagen']):
            image = request.FILES['imagen']

        nuevo_trabajador=Trabajador(nombre=request.POST['nombre'],
                                      apellidos=request.POST['apellidos'],
                                      aniosExperiencia=request.POST.get('aniosExperiencia'),
                                      tiposDeServicio=TiposDeServicio.objects.get(pk=request.POST.get('tiposDeServicio')),
                                      telefono=request.POST.get('telefono'),
                                      correo=request.POST.get('correo'),
                                      imagen=image,
                                      usuarioId=user)
        nuevo_trabajador.save()

    # return render(request, "independent/registro.html")

    return HttpResponseRedirect('/')

def detalle_trabajador(request):
    return render(request, "independent/detalle.html")

def detail(request, pk):
    trabajador = get_object_or_404(Trabajador, pk=pk)
    return HttpResponse(serializers.serialize("json", [trabajador]))

@csrf_exempt
def mostrarTrabajadores(request, tipo=""):
    if tipo == "":
      lista_trabajadores = Trabajador.objects.all()
    else:
      lista_trabajadores = Trabajador.objects.select_related().filter(tiposDeServicio__nombre__icontains=tipo)

    return HttpResponse(serializers.serialize("json", lista_trabajadores))


def login(request):
    username = request.POST.get('usrname', '')
    password = request.POST.get('psw', '')
    user = auth.authenticate(username=username, password=password)
    if user is not None:
        auth.login(request, user)
        messages.success(request, "Bienvenido al sistema {}".format(username), extra_tags="alert-success")
        return HttpResponseRedirect('/')
    else:
        messages.error(request, "¡El usuario o la contraseña son incorrectos!", extra_tags="alert-danger")
        return HttpResponseRedirect('/')


def logout(request):
    auth.logout(request)
    messages.info(request, "Cerraste sesión exitosamente", extra_tags="alert-info")
    return HttpResponseRedirect('/')