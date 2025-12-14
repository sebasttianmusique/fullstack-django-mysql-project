
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from rest_framework import viewsets
from django.utils import timezone 
# Importamos Modelos
from .models import (
    Ciudad, Usuario, Categoriaservicio, Servicio, Contrato,
    Agenda, Metodopago, Pago, Calificacion, Comentario,
    Incidencia, Notificacion
)

# Importamos Serializers 
from .serializers import (
    CiudadSerializer, UsuarioSerializer, CategoriaservicioSerializer,
    ServicioSerializer, ContratoSerializer, AgendaSerializer,
    MetodopagoSerializer, PagoSerializer, CalificacionSerializer,
    ComentarioSerializer, IncidenciaSerializer, NotificacionSerializer
)

# Importamos Formularios 
from .forms import (
    CiudadForm, UsuarioForm, CategoriaServicioForm, ServicioForm,
    ContratoForm, AgendaForm, MetodoPagoForm, PagoForm,
    CalificacionForm, ComentarioForm, IncidenciaForm, NotificacionForm
)


#            API  DRF        


class CiudadViewSet(viewsets.ModelViewSet):
    queryset = Ciudad.objects.all()
    serializer_class = CiudadSerializer

class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

class CategoriaservicioViewSet(viewsets.ModelViewSet):
    queryset = Categoriaservicio.objects.all()
    serializer_class = CategoriaservicioSerializer

class ServicioViewSet(viewsets.ModelViewSet):
    queryset = Servicio.objects.all()
    serializer_class = ServicioSerializer

class ContratoViewSet(viewsets.ModelViewSet):
    queryset = Contrato.objects.all()
    serializer_class = ContratoSerializer

class AgendaViewSet(viewsets.ModelViewSet):
    queryset = Agenda.objects.all()
    serializer_class = AgendaSerializer

class MetodopagoViewSet(viewsets.ModelViewSet):
    queryset = Metodopago.objects.all()
    serializer_class = MetodopagoSerializer

class PagoViewSet(viewsets.ModelViewSet):
    queryset = Pago.objects.all()
    serializer_class = PagoSerializer

class CalificacionViewSet(viewsets.ModelViewSet):
    queryset = Calificacion.objects.all()
    serializer_class = CalificacionSerializer

class ComentarioViewSet(viewsets.ModelViewSet):
    queryset = Comentario.objects.all()
    serializer_class = ComentarioSerializer

class IncidenciaViewSet(viewsets.ModelViewSet):
    queryset = Incidencia.objects.all()
    serializer_class = IncidenciaSerializer

class NotificacionViewSet(viewsets.ModelViewSet):
    queryset = Notificacion.objects.all()
    serializer_class = NotificacionSerializer



# CRUDS HTML       


# ----- CIUDADES -----
def lista_ciudades(request):
    ciudades = Ciudad.objects.all()
    return render(request, "tienda/ciudad_list.html", {"ciudades": ciudades})

def crear_ciudad(request):
    if request.method == "POST":
        form = CiudadForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, '¡Ciudad registrada correctamente!')
            return redirect("lista_ciudades")
    else:
        form = CiudadForm()
    return render(request, "tienda/ciudad_form.html", {"form": form})

def editar_ciudad(request, id_ciudad):
    ciudad = get_object_or_404(Ciudad, id_ciudad=id_ciudad)
    if request.method == "POST":
        form = CiudadForm(request.POST, instance=ciudad)
        if form.is_valid():
            form.save()
            messages.success(request, '¡Ciudad actualizada correctamente!')
            return redirect("lista_ciudades")
    else:
        form = CiudadForm(instance=ciudad)
    return render(request, "tienda/ciudad_form.html", {"form": form})

def eliminar_ciudad(request, id_ciudad):
    ciudad = get_object_or_404(Ciudad, id_ciudad=id_ciudad)
    if request.method == "POST":
        ciudad.delete()
        messages.success(request, '¡Ciudad eliminada correctamente!')
        # CORRECCIÓN DE INDENTACIÓN AQUÍ
        return redirect("lista_ciudades")
    return render(request, "tienda/ciudad_confirm_delete.html", {"ciudad": ciudad})


# ----- USUARIO -----
def lista_usuarios(request):
    usuarios = Usuario.objects.all()
    return render(request, "tienda/usuario_list.html", {"usuarios": usuarios})

def crear_usuario(request):
    if request.method == "POST":
        form = UsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, '¡Usuario creado correctamente!')
            return redirect("lista_usuarios")
    else:
        form = UsuarioForm()
    return render(request, "tienda/usuario_form.html", {"form": form})

def editar_usuario(request, id_usuario):
    usuario = get_object_or_404(Usuario, id_usuario=id_usuario)
    if request.method == "POST":
        form = UsuarioForm(request.POST, instance=usuario)
        if form.is_valid():
            form.save()
            messages.success(request, '¡Usuario actualizado correctamente!')
            return redirect("lista_usuarios")
    else:
        form = UsuarioForm(instance=usuario)
    return render(request, "tienda/usuario_form.html", {"form": form})

def eliminar_usuario(request, id_usuario):
    usuario = get_object_or_404(Usuario, id_usuario=id_usuario)
    if request.method == "POST":
        usuario.delete()
        messages.success(request, '¡Usuario eliminado correctamente!')
        return redirect("lista_usuarios")
    return render(request, "tienda/usuario_confirm_delete.html", {"usuario": usuario})


# ----- CATEGORÍA SERVICIO -----
def lista_categoria(request):
    categorias = Categoriaservicio.objects.all()
    return render(request, "tienda/categoria_servicio_list.html", {"categorias": categorias})

def crear_categoria(request):
    if request.method == "POST":
        form = CategoriaServicioForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, '¡Categoría creada correctamente!')
            return redirect("lista_categoria_servicio")
    else:
        form = CategoriaServicioForm()
    return render(request, "tienda/categoria_servicio_form.html", {"form": form})

def editar_categoria(request, id_categoria):
    categoria = get_object_or_404(Categoriaservicio, id_categoria=id_categoria)
    if request.method == "POST":
        form = CategoriaServicioForm(request.POST, instance=categoria)
        if form.is_valid():
            form.save()
            messages.success(request, '¡Categoría actualizada correctamente!')
            return redirect("lista_categoria_servicio")
    else:
        form = CategoriaServicioForm(instance=categoria)
    return render(request, "tienda/categoria_servicio_form.html", {"form": form})

def eliminar_categoria(request, id_categoria):
    categoria = get_object_or_404(Categoriaservicio, id_categoria=id_categoria)
    if request.method == "POST":
        categoria.delete()
        messages.success(request, '¡Categoría eliminada correctamente!')
        return redirect("lista_categoria_servicio")
    return render(request, "tienda/categoria_servicio_confirm_delete.html", {"categoria": categoria})


# ----- SERVICIO -----
def lista_servicios(request):
    servicios = Servicio.objects.all()
    return render(request, "tienda/servicio_list.html", {"servicios": servicios})

def crear_servicio(request):
    if request.method == "POST":
        form = ServicioForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, '¡Servicio creado correctamente!')
            return redirect("lista_servicios")
    else:
        form = ServicioForm()
    return render(request, "tienda/servicio_form.html", {"form": form})

def editar_servicio(request, id_servicio):
    servicio = get_object_or_404(Servicio, id_servicio=id_servicio)
    if request.method == "POST":
        form = ServicioForm(request.POST, instance=servicio)
        if form.is_valid():
            form.save()
            messages.success(request, '¡Servicio actualizado correctamente!')
            return redirect("lista_servicios")
    else:
        form = ServicioForm(instance=servicio)
    return render(request, "tienda/servicio_form.html", {"form": form})

def eliminar_servicio(request, id_servicio):
    servicio = get_object_or_404(Servicio, id_servicio=id_servicio)
    if request.method == "POST":
        servicio.delete()
        messages.success(request, '¡Servicio eliminado correctamente!')
        return redirect("lista_servicios")
    return render(request, "tienda/servicio_confirm_delete.html", {"servicio": servicio})


# ----- CONTRATO -----
def lista_contratos(request):
    contratos = Contrato.objects.all()
    return render(request, "tienda/contrato_list.html", {"contratos": contratos})

def crear_contrato(request):
    if request.method == "POST":
        form = ContratoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, '¡Contrato registrado correctamente!')
            return redirect("lista_contratos")
    else:
        form = ContratoForm()
    return render(request, "tienda/contrato_form.html", {"form": form})

def editar_contrato(request, id_contrato):
    contrato = get_object_or_404(Contrato, id_contrato=id_contrato)
    if request.method == "POST":
        form = ContratoForm(request.POST, instance=contrato)
        if form.is_valid():
            form.save()
            messages.success(request, '¡Contrato actualizado correctamente!')
            return redirect("lista_contratos")
    else:
        form = ContratoForm(instance=contrato)
    return render(request, "tienda/contrato_form.html", {"form": form})

def eliminar_contrato(request, id_contrato):
    contrato = get_object_or_404(Contrato, id_contrato=id_contrato)
    if request.method == "POST":
        contrato.delete()
        messages.success(request, '¡Contrato eliminado correctamente!')
        return redirect("lista_contratos")
    return render(request, "tienda/contrato_confirm_delete.html", {"contrato": contrato})


# ----- AGENDA -----
def lista_agendas(request):
    agendas = Agenda.objects.all()
    return render(request, "tienda/agenda_list.html", {"agendas": agendas})

def crear_agenda(request):
    if request.method == "POST":
        form = AgendaForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, '¡Cita agendada correctamente!')
            return redirect("lista_agendas")
    else:
        form = AgendaForm()
    return render(request, "tienda/agenda_form.html", {"form": form})

def editar_agenda(request, id_agenda):
    agenda = get_object_or_404(Agenda, id_agenda=id_agenda)
    if request.method == "POST":
        form = AgendaForm(request.POST, instance=agenda)
        if form.is_valid():
            form.save()
            messages.success(request, '¡Cita actualizada correctamente!')
            return redirect("lista_agendas")
    else:
        form = AgendaForm(instance=agenda)
    return render(request, "tienda/agenda_form.html", {"form": form})

def eliminar_agenda(request, id_agenda):
    agenda = get_object_or_404(Agenda, id_agenda=id_agenda)
    if request.method == "POST":
        agenda.delete()
        messages.success(request, '¡Cita eliminada de la agenda!')
        return redirect("lista_agendas")
    return render(request, "tienda/agenda_confirm_delete.html", {"agenda": agenda})


# ----- MÉTODO DE PAGO -----
def lista_metodos(request):
    metodos = Metodopago.objects.all()
    return render(request, "tienda/metodo_pago_list.html", {"metodos": metodos})

def crear_metodo(request):
    if request.method == "POST":
        form = MetodoPagoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, '¡Método de pago creado correctamente!')
            return redirect("lista_metodos")
    else:
        form = MetodoPagoForm()
    return render(request, "tienda/metodo_pago_form.html", {"form": form})

def editar_metodo(request, id_metodo_pago):
    metodo = get_object_or_404(Metodopago, id_metodo_pago=id_metodo_pago)
    if request.method == "POST":
        form = MetodoPagoForm(request.POST, instance=metodo)
        if form.is_valid():
            form.save()
            messages.success(request, '¡Método de pago actualizado correctamente!')
            return redirect("lista_metodos")
    else:
        form = MetodoPagoForm(instance=metodo)
    return render(request, "tienda/metodo_pago_form.html", {"form": form})

def eliminar_metodo(request, id_metodo_pago):
    metodo = get_object_or_404(Metodopago, id_metodo_pago=id_metodo_pago)
    if request.method == "POST":
        metodo.delete()
        messages.success(request, '¡Método de pago eliminado correctamente!')
        return redirect("lista_metodos")
    return render(request, "tienda/metodo_pago_confirm_delete.html", {"metodo": metodo})


# ----- PAGO -----
def lista_pagos(request):
    pagos = Pago.objects.all()
    return render(request, "tienda/pago_list.html", {"pagos": pagos})

def crear_pago(request):
    if request.method == "POST":
        form = PagoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, '¡Pago registrado correctamente!')
            return redirect("lista_pagos")
    else:
        form = PagoForm()
    return render(request, "tienda/pago_form.html", {"form": form})

def editar_pago(request, id_pago):
    pago = get_object_or_404(Pago, id_pago=id_pago)
    if request.method == "POST":
        form = PagoForm(request.POST, instance=pago)
        if form.is_valid():
            form.save()
            messages.success(request, '¡Pago actualizado correctamente!')
            return redirect("lista_pagos")
    else:
        form = PagoForm(instance=pago)
    return render(request, "tienda/pago_form.html", {"form": form})

def eliminar_pago(request, id_pago):
    pago = get_object_or_404(Pago, id_pago=id_pago)
    if request.method == "POST":
        pago.delete()
        messages.success(request, '¡Pago eliminado correctamente!')
        return redirect("lista_pagos")
    return render(request, "tienda/pago_confirm_delete.html", {"pago": pago})


# ----- CALIFICACIÓN -----
def lista_calificaciones(request):
    calificaciones = Calificacion.objects.all()
    return render(request, "tienda/calificacion_list.html", {"calificaciones": calificaciones})

def crear_calificacion(request):
    if request.method == "POST":
        form = CalificacionForm(request.POST)
        if form.is_valid():
            
            calificacion_instance = form.save(commit=False) 
            
            
            calificacion_instance.fecha_calificacion = timezone.now()
            
            
            calificacion_instance.save()
            
            messages.success(request, '¡Calificación enviada correctamente!')
            return redirect("lista_calificaciones")
    else:
        form = CalificacionForm()
    return render(request, "tienda/calificacion_form.html", {"form": form})

def editar_calificacion(request, id_calificacion):
    calificacion = get_object_or_404(Calificacion, id_calificacion=id_calificacion)
    if request.method == "POST":
        form = CalificacionForm(request.POST, instance=calificacion)
        if form.is_valid():
            form.save()
            messages.success(request, '¡Calificación actualizada correctamente!')
            return redirect("lista_calificaciones")
    else:
        form = CalificacionForm(instance=calificacion)
    return render(request, "tienda/calificacion_form.html", {"form": form})

def eliminar_calificacion(request, id_calificacion):
    calificacion = get_object_or_404(Calificacion, id_calificacion=id_calificacion)
    if request.method == "POST":
        calificacion.delete()
        messages.success(request, '¡Calificación eliminada correctamente!')
        return redirect("lista_calificaciones")
    return render(request, "tienda/calificacion_confirm_delete.html", {"calificacion": calificacion})


# ----- COMENTARIO -----
def lista_comentarios(request):
    comentarios = Comentario.objects.all()
    return render(request, "tienda/comentario_list.html", {"comentarios": comentarios})

def crear_comentario(request):
    if request.method == "POST":
        form = ComentarioForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, '¡Comentario publicado correctamente!')
            return redirect("lista_comentarios")
    else:
        form = ComentarioForm()
    return render(request, "tienda/comentario_form.html", {"form": form})

def editar_comentario(request, id_comentario):
    comentario = get_object_or_404(Comentario, id_comentario=id_comentario)
    if request.method == "POST":
        form = ComentarioForm(request.POST, instance=comentario)
        if form.is_valid():
            form.save()
            messages.success(request, '¡Comentario actualizado correctamente!')
            return redirect("lista_comentarios")
    else:
        form = ComentarioForm(instance=comentario)
    return render(request, "tienda/comentario_form.html", {"form": form})

def eliminar_comentario(request, id_comentario):
    comentario = get_object_or_404(Comentario, id_comentario=id_comentario)
    if request.method == "POST":
        comentario.delete()
        messages.success(request, '¡Comentario eliminado correctamente!')
        return redirect("lista_comentarios")
    return render(request, "tienda/comentario_confirm_delete.html", {"comentario": comentario})


# ----- INCIDENCIA -----
def lista_incidencias(request):
    incidencias = Incidencia.objects.all()
    return render(request, "tienda/incidencia_list.html", {"incidencias": incidencias})

def crear_incidencia(request):
    if request.method == "POST":
        form = IncidenciaForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, '¡Incidencia reportada correctamente!')
            return redirect("lista_incidencias")
    else:
        form = IncidenciaForm()
    return render(request, "tienda/incidencia_form.html", {"form": form})

def editar_incidencia(request, id_incidencia):
    incidencia = get_object_or_404(Incidencia, id_incidencia=id_incidencia)
    if request.method == "POST":
        form = IncidenciaForm(request.POST, instance=incidencia)
        if form.is_valid():
            form.save()
            messages.success(request, '¡Incidencia actualizada correctamente!')
            return redirect("lista_incidencias")
    else:
        form = IncidenciaForm(instance=incidencia)
    return render(request, "tienda/incidencia_form.html", {"form": form})

def eliminar_incidencia(request, id_incidencia):
    incidencia = get_object_or_404(Incidencia, id_incidencia=id_incidencia)
    if request.method == "POST":
        incidencia.delete()
        messages.success(request, '¡Incidencia eliminada correctamente!')
        return redirect("lista_incidencias")
    return render(request, "tienda/incidencia_confirm_delete.html", {"incidencia": incidencia})


# ----- NOTIFICACIÓN -----
def lista_notificaciones(request):
    notificaciones = Notificacion.objects.all()
    return render(request, "tienda/notificacion_list.html", {"notificaciones": notificaciones})

def crear_notificacion(request):
    if request.method == "POST":
        form = NotificacionForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, '¡Notificación enviada correctamente!')
            return redirect("lista_notificaciones")
    else:
        form = NotificacionForm()
    return render(request, "tienda/notificacion_form.html", {"form": form})

def editar_notificacion(request, id_notificacion):
    notificacion = get_object_or_404(Notificacion, id_notificacion=id_notificacion)
    if request.method == "POST":
        form = NotificacionForm(request.POST, instance=notificacion)
        if form.is_valid():
            form.save()
            messages.success(request, '¡Notificación actualizada correctamente!')
            return redirect("lista_notificaciones")
    else:
        form = NotificacionForm(instance=notificacion)
    return render(request, "tienda/notificacion_form.html", {"form": form})

def eliminar_notificacion(request, id_notificacion):
    notificacion = get_object_or_404(Notificacion, id_notificacion=id_notificacion)
    if request.method == "POST":
        notificacion.delete()
        messages.success(request, '¡Notificación eliminada correctamente!')
        return redirect("lista_notificaciones")
    return render(request, "tienda/notificacion_confirm_delete.html", {"notificacion": notificacion})