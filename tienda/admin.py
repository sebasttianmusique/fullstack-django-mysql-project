
from django.contrib import admin
from .models import (
    Usuario, Profesional, Cliente, Administrador,
    Ciudad, Categoriaservicio, Servicio,
    Contrato, Agenda, Metodopago, Pago,
    Calificacion, Comentario, Incidencia, Notificacion
)

# USUARIO
@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ("id_usuario", "nombre", "apellido", "correo_electronico", "tipo_usuario", "estado", "id_ciudad")
    search_fields = ("nombre", "apellido", "correo_electronico")
    list_filter = ("tipo_usuario", "estado", "id_ciudad")
    ordering = ("id_usuario",)


# PROFESIONAL
@admin.register(Profesional)
class ProfesionalAdmin(admin.ModelAdmin):
    list_display = ("id_profesional", "experiencia", "calificacion_promedio")
    search_fields = ("id_profesional__nombre", "id_profesional__apellido")
    list_filter = ("calificacion_promedio",)
    ordering = ("id_profesional",)


# CLIENTE
@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ("id_cliente", "historial_pedidos", "calificacion_promedio", "fecha_ultima_solicitud")
    search_fields = ("id_cliente__nombre", "id_cliente__apellido")
    ordering = ("id_cliente",)


# ADMINISTRADOR
@admin.register(Administrador)
class AdministradorAdmin(admin.ModelAdmin):
    list_display = ("id_administrador", "rol")
    search_fields = ("id_administrador__nombre", "id_administrador__apellido")
    ordering = ("id_administrador",)


# CIUDAD
@admin.register(Ciudad)
class CiudadAdmin(admin.ModelAdmin):
    list_display = ("id_ciudad", "nombre_ciudad", "departamento")
    search_fields = ("nombre_ciudad", "departamento")
    ordering = ("nombre_ciudad",)


# CATEGORIA SERVICIO
@admin.register(Categoriaservicio)
class CategoriaServicioAdmin(admin.ModelAdmin):
    list_display = ("id_categoria", "nombre_categoria")
    search_fields = ("nombre_categoria",)
    ordering = ("nombre_categoria",)


# SERVICIO
@admin.register(Servicio)
class ServicioAdmin(admin.ModelAdmin):
    list_display = ("id_servicio", "nombre_servicio", "precio_base", "duracion_estimada", "garantia_meses", "id_categoria")
    search_fields = ("nombre_servicio",)
    list_filter = ("id_categoria",)
    ordering = ("id_servicio",)


# CONTRATO
@admin.register(Contrato)
class ContratoAdmin(admin.ModelAdmin):
    list_display = ("id_contrato", "id_cliente", "id_profesional", "id_servicio", "fecha_inicio", "estado_contrato")
    search_fields = ("id_cliente__nombre", "id_profesional__nombre")
    list_filter = ("estado_contrato", "fecha_inicio")
    ordering = ("id_contrato",)


# AGENDA
@admin.register(Agenda)
class AgendaAdmin(admin.ModelAdmin):
    list_display = ("id_agenda", "id_cliente", "id_profesional", "id_servicio", "id_ciudad", "fecha_cita", "hora_cita", "estado_cita")
    list_filter = ("estado_cita", "id_ciudad", "fecha_cita")
    ordering = ("id_agenda",)


# METODO PAGO
@admin.register(Metodopago)
class MetodoPagoAdmin(admin.ModelAdmin):
    list_display = ("id_metodo_pago", "nombre_metodo")
    search_fields = ("nombre_metodo",)
    ordering = ("id_metodo_pago",)


# PAGO
@admin.register(Pago)
class PagoAdmin(admin.ModelAdmin):
    list_display = ("id_pago", "id_contrato", "id_metodo_pago", "monto", "fecha_pago", "estado_pago")
    list_filter = ("estado_pago", "fecha_pago")
    search_fields = ("id_contrato__id_cliente__nombre",)
    ordering = ("id_pago",)


# CALIFICACION
@admin.register(Calificacion)
class CalificacionAdmin(admin.ModelAdmin):
    list_display = ("id_calificacion", "id_cliente", "id_profesional", "puntaje", "fecha_calificacion")
    list_filter = ("puntaje", "fecha_calificacion")
    ordering = ("id_calificacion",)


# COMENTARIO
@admin.register(Comentario)
class ComentarioAdmin(admin.ModelAdmin):
    list_display = ("id_comentario", "id_cliente", "texto_comentario", "fecha_comentario")
    search_fields = ("texto_comentario",)
    ordering = ("id_comentario",)


# INCIDENCIA
@admin.register(Incidencia)
class IncidenciaAdmin(admin.ModelAdmin):
    list_display = ("id_incidencia", "tipo_incidencia", "estado_incidencia", "fecha_creacion", "fecha_resolucion")
    list_filter = ("estado_incidencia", "tipo_incidencia")
    ordering = ("id_incidencia",)


# NOTIFICACION
@admin.register(Notificacion)
class NotificacionAdmin(admin.ModelAdmin):
    list_display = ("id_notificacion", "mensaje", "tipo_notificacion", "estado_lectura", "fecha_envio")
    list_filter = ("tipo_notificacion", "estado_lectura", "fecha_envio")
    search_fields = ("mensaje",)
    ordering = ("id_notificacion",)
