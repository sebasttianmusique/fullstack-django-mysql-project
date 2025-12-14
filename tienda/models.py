
# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
# * Rearrange models' order
# * Make sure each model has one field with primary_key=True
# * Make sure each ForeignKey and OneToOneField has on_delete set to the desired behavior
# * Remove managed = False lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models

PUNTAJES = (
    (1, '⭐ Mala'),
    (2, '⭐⭐ Regular'),
    (3, '⭐⭐⭐ Buena'),
    (4, '⭐⭐⭐⭐ Muy Buena'),
    (5, '⭐⭐⭐⭐⭐ Excelente'),
)


class Administrador(models.Model):
    id_administrador = models.OneToOneField('Usuario', models.DO_NOTHING, db_column='id_administrador', primary_key=True)
    rol = models.CharField(max_length=11)

    class Meta:
        managed = False
        db_table = 'Administrador'

    def __str__(self):
        return f"Administrador {self.id_administrador.nombre}"


class Agenda(models.Model):
    id_agenda = models.AutoField(primary_key=True)
    id_cliente = models.ForeignKey('Cliente', models.DO_NOTHING, db_column='id_cliente')
    id_profesional = models.ForeignKey('Profesional', models.DO_NOTHING, db_column='id_profesional')
    id_servicio = models.ForeignKey('Servicio', models.DO_NOTHING, db_column='id_servicio')
    id_ciudad = models.ForeignKey('Ciudad', models.DO_NOTHING, db_column='id_ciudad', blank=True, null=True)
    fecha_cita = models.DateField()
    hora_cita = models.TimeField()
    estado_cita = models.CharField(max_length=30)  
    class Meta:
        managed = False
        db_table = 'Agenda'

    def __str__(self):

        try:
            cliente_nombre = f"{self.id_cliente.id_cliente.nombre} {self.id_cliente.id_cliente.apellido}"
        except:
            cliente_nombre = "Cliente Desconocido"
        return f"Cita {self.fecha_cita} {self.hora_cita} - {cliente_nombre}"


class Calificacion(models.Model):
    id_calificacion = models.AutoField(primary_key=True)
    id_cliente = models.ForeignKey('Cliente', models.DO_NOTHING, db_column='id_cliente')
    id_profesional = models.ForeignKey('Profesional', models.DO_NOTHING, db_column='id_profesional')
    id_servicio = models.ForeignKey('Servicio', models.DO_NOTHING, db_column='id_servicio', blank=True, null=True)
    puntaje = models.IntegerField(choices=PUNTAJES)
    fecha_calificacion = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Calificacion'

    def __str__(self):
        return f"Calificación {self.get_puntaje_display()} de {self.id_cliente.id_cliente.nombre}"


class Categoriaservicio(models.Model):
    id_categoria = models.AutoField(primary_key=True)
    nombre_categoria = models.CharField(unique=True, max_length=120)
    descripcion_categoria = models.CharField(max_length=300, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'CategoriaServicio'

    def __str__(self):
        return self.nombre_categoria


class Ciudad(models.Model):
    id_ciudad = models.AutoField(primary_key=True)
    nombre_ciudad = models.CharField(max_length=120)
    departamento = models.CharField(max_length=120)

    class Meta:
        managed = False
        db_table = 'Ciudad'
        unique_together = (('nombre_ciudad', 'departamento'),)

    def __str__(self):
        return f"{self.nombre_ciudad}, {self.departamento}"


class Cliente(models.Model):
    id_cliente = models.OneToOneField('Usuario', models.DO_NOTHING, db_column='id_cliente', primary_key=True)
    preferencias_servicio = models.CharField(max_length=255, blank=True, null=True)
    historial_pedidos = models.IntegerField(blank=True, null=True)
    calificacion_promedio = models.DecimalField(max_digits=3, decimal_places=2, blank=True, null=True)
    solicitudes_especiales = models.CharField(max_length=255, blank=True, null=True)
    fecha_ultima_solicitud = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Cliente'

    def __str__(self):
        try:
            return f"Cliente: {self.id_cliente.nombre} {self.id_cliente.apellido}"
        except AttributeError:
            return f"Cliente ID: {self.pk}"


class Comentario(models.Model):
    id_comentario = models.AutoField(primary_key=True)
    id_cliente = models.ForeignKey(Cliente, models.DO_NOTHING, db_column='id_cliente')
    id_calificacion = models.ForeignKey(Calificacion, models.DO_NOTHING, db_column='id_calificacion', blank=True, null=True)
    texto_comentario = models.CharField(max_length=600)
    fecha_comentario = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'Comentario'


class Contrato(models.Model):
    id_contrato = models.AutoField(primary_key=True)
    id_cliente = models.ForeignKey(Cliente, models.DO_NOTHING, db_column='id_cliente')
    id_profesional = models.ForeignKey('Profesional', models.DO_NOTHING, db_column='id_profesional')
    id_servicio = models.ForeignKey('Servicio', models.DO_NOTHING, db_column='id_servicio')
    fecha_inicio = models.DateTimeField()
    estado_contrato = models.CharField(max_length=10)

    class Meta:
        managed = False
        db_table = 'Contrato'


class Incidencia(models.Model):
    id_incidencia = models.AutoField(primary_key=True)
    id_cliente = models.ForeignKey(Cliente, models.DO_NOTHING, db_column='id_cliente', blank=True, null=True)
    id_profesional = models.ForeignKey('Profesional', models.DO_NOTHING, db_column='id_profesional', blank=True, null=True)
    id_servicio = models.ForeignKey('Servicio', models.DO_NOTHING, db_column='id_servicio', blank=True, null=True)
    id_administrador = models.ForeignKey(Administrador, models.DO_NOTHING, db_column='id_administrador', blank=True, null=True)
    tipo_incidencia = models.CharField(max_length=10)
    descripcion = models.CharField(max_length=600)
    estado_incidencia = models.CharField(max_length=10)
    fecha_creacion = models.DateTimeField()
    fecha_resolucion = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Incidencia'


class Metodopago(models.Model):
    id_metodo_pago = models.AutoField(primary_key=True)
    nombre_metodo = models.CharField(max_length=8)
    descripcion = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'MetodoPago'

    def __str__(self):
        return self.nombre_metodo


class Notificacion(models.Model):
    id_notificacion = models.AutoField(primary_key=True)
    mensaje = models.CharField(max_length=400)
    fecha_envio = models.DateTimeField()
    tipo_notificacion = models.CharField(max_length=12)
    estado_lectura = models.CharField(max_length=8)
    id_cliente = models.ForeignKey(Cliente, models.DO_NOTHING, db_column='id_cliente', blank=True, null=True)
    id_profesional = models.ForeignKey('Profesional', models.DO_NOTHING, db_column='id_profesional', blank=True, null=True)
    id_administrador = models.ForeignKey(Administrador, models.DO_NOTHING, db_column='id_administrador', blank=True, null=True)
    id_incidencia = models.ForeignKey(Incidencia, models.DO_NOTHING, db_column='id_incidencia', blank=True, null=True)
    id_pago = models.ForeignKey('Pago', models.DO_NOTHING, db_column='id_pago', blank=True, null=True)
    id_agenda = models.ForeignKey(Agenda, models.DO_NOTHING, db_column='id_agenda', blank=True, null=True)
    id_comentario = models.ForeignKey(Comentario, models.DO_NOTHING, db_column='id_comentario', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Notificacion'


class Pago(models.Model):
    id_pago = models.AutoField(primary_key=True)
    id_contrato = models.ForeignKey(Contrato, models.DO_NOTHING, db_column='id_contrato')
    id_metodo_pago = models.ForeignKey(Metodopago, models.DO_NOTHING, db_column='id_metodo_pago')
    id_agenda = models.OneToOneField(Agenda, models.DO_NOTHING, db_column='id_agenda', blank=True, null=True)
    monto = models.DecimalField(max_digits=12, decimal_places=2)
    fecha_pago = models.DateTimeField()
    estado_pago = models.CharField(max_length=9)

    class Meta:
        managed = False
        db_table = 'Pago'


class Profesional(models.Model):
    id_profesional = models.OneToOneField('Usuario', models.DO_NOTHING, db_column='id_profesional', primary_key=True)
    descripcion_perfil = models.CharField(max_length=500, blank=True, null=True)
    experiencia = models.CharField(max_length=200, blank=True, null=True)
    certificaciones = models.CharField(max_length=500, blank=True, null=True)
    calificacion_promedio = models.DecimalField(max_digits=3, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Profesional'

    def __str__(self):
        try:
            return f"Profesional: {self.id_profesional.nombre} {self.id_profesional.apellido}"
        except AttributeError:
            return f"Profesional ID: {self.pk}"


class Servicio(models.Model):
    id_servicio = models.AutoField(primary_key=True)
    nombre_servicio = models.CharField(unique=True, max_length=150)
    descripcion = models.CharField(max_length=500, blank=True, null=True)
    precio_base = models.DecimalField(max_digits=12, decimal_places=2)
    duracion_estimada = models.IntegerField(blank=True, null=True)
    garantia_meses = models.IntegerField(blank=True, null=True)
    id_categoria = models.ForeignKey(Categoriaservicio, models.DO_NOTHING, db_column='id_categoria', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Servicio'

    def __str__(self):
        return self.nombre_servicio


class Usuario(models.Model):
    id_usuario = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    correo_electronico = models.CharField(unique=True, max_length=180)
    contrasena = models.CharField(max_length=255)
    telefono = models.CharField(max_length=30, blank=True, null=True)
    direccion = models.CharField(max_length=200, blank=True, null=True)
    tipo_usuario = models.CharField(max_length=13)
    fecha_registro = models.DateTimeField()
    estado = models.CharField(max_length=9)
    id_ciudad = models.ForeignKey(Ciudad, models.DO_NOTHING, db_column='id_ciudad', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'Usuario'

    def __str__(self):
        return f"{self.nombre} {self.apellido}"


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'