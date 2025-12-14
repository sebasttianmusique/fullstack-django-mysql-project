
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from tienda.views import (
    CiudadViewSet, UsuarioViewSet, CategoriaservicioViewSet,
    ServicioViewSet, ContratoViewSet, AgendaViewSet,
    MetodopagoViewSet, PagoViewSet, CalificacionViewSet,
    ComentarioViewSet, IncidenciaViewSet, NotificacionViewSet,

    lista_ciudades, crear_ciudad, editar_ciudad, eliminar_ciudad,
    lista_usuarios, crear_usuario, editar_usuario, eliminar_usuario,
    lista_categoria, crear_categoria, editar_categoria, eliminar_categoria,
    lista_servicios, crear_servicio, editar_servicio, eliminar_servicio,
    lista_contratos, crear_contrato, editar_contrato, eliminar_contrato,
    lista_agendas, crear_agenda, editar_agenda, eliminar_agenda,
    lista_metodos, crear_metodo, editar_metodo, eliminar_metodo,
    lista_pagos, crear_pago, editar_pago, eliminar_pago,
    lista_calificaciones, crear_calificacion, editar_calificacion, eliminar_calificacion,
    lista_comentarios, crear_comentario, editar_comentario, eliminar_comentario,
    lista_incidencias, crear_incidencia, editar_incidencia, eliminar_incidencia,
    lista_notificaciones, crear_notificacion, editar_notificacion, eliminar_notificacion,
)

#  API ROUTER (DRF) 
router = routers.DefaultRouter()
router.register(r'ciudades', CiudadViewSet)
router.register(r'usuarios', UsuarioViewSet)
router.register(r'categorias', CategoriaservicioViewSet)
router.register(r'servicios', ServicioViewSet)
router.register(r'contratos', ContratoViewSet)
router.register(r'agendas', AgendaViewSet)
router.register(r'metodos', MetodopagoViewSet)
router.register(r'pagos', PagoViewSet)
router.register(r'calificaciones', CalificacionViewSet)
router.register(r'comentarios', ComentarioViewSet)
router.register(r'incidencias', IncidenciaViewSet)
router.register(r'notificaciones', NotificacionViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),

    # CRUDS HTML 

    # CIUDADES
    path("ciudades/", lista_ciudades, name="lista_ciudades"),
    path("ciudades/crear/", crear_ciudad, name="crear_ciudad"),
    path("ciudades/editar/<int:id_ciudad>/", editar_ciudad, name="editar_ciudad"),
    path("ciudades/eliminar/<int:id_ciudad>/", eliminar_ciudad, name="eliminar_ciudad"),

    # USUARIOS
    path("usuarios/", lista_usuarios, name="lista_usuarios"),
    path("usuarios/crear/", crear_usuario, name="crear_usuario"),
    path("usuarios/editar/<int:id_usuario>/", editar_usuario, name="editar_usuario"),
    path("usuarios/eliminar/<int:id_usuario>/", eliminar_usuario, name="eliminar_usuario"),

    # CATEGORÍAS
    path("categorias/", lista_categoria, name="lista_categoria_servicio"),
    path("categorias/crear/", crear_categoria, name="crear_categoria_servicio"),
    path("categorias/editar/<int:id_categoria>/", editar_categoria, name="editar_categoria_servicio"),
    path("categorias/eliminar/<int:id_categoria>/", eliminar_categoria, name="eliminar_categoria_servicio"),

    # SERVICIOS
    path("servicios/", lista_servicios, name="lista_servicios"),
    path("servicios/crear/", crear_servicio, name="crear_servicio"),
    path("servicios/editar/<int:id_servicio>/", editar_servicio, name="editar_servicio"),
    path("servicios/eliminar/<int:id_servicio>/", eliminar_servicio, name="eliminar_servicio"),

    # CONTRATOS
    path("contratos/", lista_contratos, name="lista_contratos"),
    path("contratos/crear/", crear_contrato, name="crear_contrato"),
    path("contratos/editar/<int:id_contrato>/", editar_contrato, name="editar_contrato"),
    path("contratos/eliminar/<int:id_contrato>/", eliminar_contrato, name="eliminar_contrato"),

    # AGENDAS
    path("agendas/", lista_agendas, name="lista_agendas"),
    path("agendas/crear/", crear_agenda, name="crear_agenda"),
    path("agendas/editar/<int:id_agenda>/", editar_agenda, name="editar_agenda"),
    path("agendas/eliminar/<int:id_agenda>/", eliminar_agenda, name="eliminar_agenda"),

    # MÉTODOS DE PAGO
    path("metodos/", lista_metodos, name="lista_metodos"),
    path("metodos/crear/", crear_metodo, name="crear_metodo"),
    path("metodos/editar/<int:id_metodo_pago>/", editar_metodo, name="editar_metodo"),
    path("metodos/eliminar/<int:id_metodo_pago>/", eliminar_metodo, name="eliminar_metodo"),

    # PAGOS
    path("pagos/", lista_pagos, name="lista_pagos"),
    path("pagos/crear/", crear_pago, name="crear_pago"),
    path("pagos/editar/<int:id_pago>/", editar_pago, name="editar_pago"),
    path("pagos/eliminar/<int:id_pago>/", eliminar_pago, name="eliminar_pago"),

    # CALIFICACIONES
    path("calificaciones/", lista_calificaciones, name="lista_calificaciones"),
    path("calificaciones/crear/", crear_calificacion, name="crear_calificacion"),
    path("calificaciones/editar/<int:id_calificacion>/", editar_calificacion, name="editar_calificacion"),
    path("calificaciones/eliminar/<int:id_calificacion>/", eliminar_calificacion, name="eliminar_calificacion"),

    # COMENTARIOS
    path("comentarios/", lista_comentarios, name="lista_comentarios"),
    path("comentarios/crear/", crear_comentario, name="crear_comentario"),
    path("comentarios/editar/<int:id_comentario>/", editar_comentario, name="editar_comentario"),
    path("comentarios/eliminar/<int:id_comentario>/", eliminar_comentario, name="eliminar_comentario"),

    # INCIDENCIAS
    path("incidencias/", lista_incidencias, name="lista_incidencias"),
    path("incidencias/crear/", crear_incidencia, name="crear_incidencia"),
    path("incidencias/editar/<int:id_incidencia>/", editar_incidencia, name="editar_incidencia"),
    path("incidencias/eliminar/<int:id_incidencia>/", eliminar_incidencia, name="eliminar_incidencia"),

    # NOTIFICACIONES
    path("notificaciones/", lista_notificaciones, name="lista_notificaciones"),
    path("notificaciones/crear/", crear_notificacion, name="crear_notificacion"),
    path("notificaciones/editar/<int:id_notificacion>/", editar_notificacion, name="editar_notificacion"),
    path("notificaciones/eliminar/<int:id_notificacion>/", eliminar_notificacion, name="eliminar_notificacion"),

    # API DRF
    path("api/", include(router.urls)),
]
  
    
    
    
    
    
    
    
    
    
    
    
    
    

