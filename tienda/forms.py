
from django import forms
from django.core.exceptions import ValidationError
from django.utils import timezone 
from .models import (
    Ciudad, Usuario, Categoriaservicio, Servicio, Contrato, Agenda,
    Metodopago, Pago, Calificacion, Comentario, Incidencia, Notificacion
)


# CIUDAD

class CiudadForm(forms.ModelForm):
    class Meta:
        model = Ciudad
        fields = ['nombre_ciudad', 'departamento']



# USUARIO

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = [
            'nombre', 'apellido', 'correo_electronico', 'contrasena',
            'telefono', 'direccion', 'tipo_usuario',
            'fecha_registro',   
            'estado', 'id_ciudad'
        ]


# CATEGORIA SERVICIO

class CategoriaServicioForm(forms.ModelForm):

    CATEGORIAS_PROHIBIDAS = [
        "veterinario", "medicina", "salud", "derecho", "legal", 
        "educacion", "contabilidad", "financiero", "restaurante", "cocina"
    ]
    
    class Meta:
        model = Categoriaservicio
        fields = ['nombre_categoria', 'descripcion_categoria']
    
    def clean_nombre_categoria(self):
        """
        Método de validación que verifica si el nombre de la categoría 
        está en la lista de servicios prohibidos.
        """
        nombre = self.cleaned_data.get("nombre_categoria")
        nombre_limpio = nombre.strip().lower()
        
        for prohibida in self.CATEGORIAS_PROHIBIDAS:
            if prohibida in nombre_limpio:
                raise ValidationError(
                    f"La categoría '{nombre}' no pertenece al rubro de Ayuda Express. Por favor, ingrese un servicio de hogar, mantenimiento o tecnología."
                )
        return nombre


# SERVICIO

class ServicioForm(forms.ModelForm):
    class Meta:
        model = Servicio
        fields = [
            'nombre_servicio', 'descripcion', 'precio_base',
            'duracion_estimada', 'garantia_meses', 'id_categoria'
        ]



# CONTRATO 

class ContratoForm(forms.ModelForm):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        if not self.instance.pk:

            self.fields['fecha_inicio'].initial = timezone.now().date()

    class Meta:
        model = Contrato
        fields = [
            'id_cliente', 'id_profesional',
            'id_servicio', 'fecha_inicio', 'estado_contrato'
        ]
        
        widgets = {
            'fecha_inicio': forms.DateInput(attrs={'type': 'date'}),
        }


# AGENDA

class AgendaForm(forms.ModelForm):
    class Meta:
        model = Agenda
        fields = [
            'id_cliente', 'id_profesional', 'id_servicio',
            'id_ciudad', 'fecha_cita', 'hora_cita', 'estado_cita'
        ]



# METODO DE PAGO

class MetodoPagoForm(forms.ModelForm):
    class Meta:
        model = Metodopago
        fields = ['nombre_metodo', 'descripcion']



# PAGO

class PagoForm(forms.ModelForm):
    class Meta:
        model = Pago
        fields = [
            'id_contrato', 'id_metodo_pago', 'id_agenda',
            'monto', 'fecha_pago', 'estado_pago'
        ]



# CALIFICACIÓN


class CalificacionForm(forms.ModelForm):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        if not self.instance.pk:

            self.fields['fecha_calificacion'].initial = timezone.now().date()
            
    class Meta:
        model = Calificacion
        fields = [
            'id_cliente', 'id_profesional', 'id_servicio',
            'puntaje', 
            'fecha_calificacion' 
        ]

        widgets = {
            'fecha_calificacion': forms.DateInput(attrs={'type': 'date'}),
        }



# COMENTARIO 

class ComentarioForm(forms.ModelForm):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        if not self.instance.pk:

            self.fields['fecha_comentario'].initial = timezone.now().date()

        
    class Meta:
        model = Comentario
        fields = [
            'id_cliente', 
            'id_calificacion',
            'texto_comentario',
            'fecha_comentario' 
        ]

        widgets = {
            
            'fecha_comentario': forms.DateInput(attrs={'type': 'date'}), 
        }



# INCIDENCIA

class IncidenciaForm(forms.ModelForm):
    class Meta:
        model = Incidencia
        fields = [
            'id_cliente', 'id_profesional', 'id_servicio', 'id_administrador',
            'tipo_incidencia', 'descripcion', 'estado_incidencia',
            'fecha_creacion', 'fecha_resolucion'
        ]



# NOTIFICACION


class NotificacionForm(forms.ModelForm):
    class Meta:
        model = Notificacion
        fields = [
            'mensaje', 'fecha_envio', 'tipo_notificacion', 'estado_lectura',
            'id_cliente', 'id_profesional', 'id_administrador',
            'id_incidencia', 'id_pago', 'id_agenda', 'id_comentario'
        ]