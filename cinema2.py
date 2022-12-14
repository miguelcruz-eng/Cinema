# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Ator(models.Model):
    id_ator = models.IntegerField(primary_key=True)
    nome = models.TextField(blank=True, null=True)
    data_nascimento_ator = models.DateField(blank=True, null=True)
    idade = models.IntegerField(blank=True, null=True)
    biografia = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ator'


class AtorFilme(models.Model):
    ator = models.OneToOneField(Ator, models.DO_NOTHING, primary_key=True)
    filme = models.ForeignKey('Filme', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'ator_filme'
        unique_together = (('ator', 'filme'),)


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


class CinemaFilme(models.Model):
    id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=255)
    description = models.TextField()
    lancamento = models.DateField()
    tipo = models.CharField(max_length=10)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    foto = models.TextField()
    cartaz = models.TextField()

    class Meta:
        managed = False
        db_table = 'cinema_filme'


class Clientes(models.Model):
    id_cliente = models.IntegerField(primary_key=True)
    i_tipo_cliente = models.ForeignKey('Tipocliente', models.DO_NOTHING, db_column='i_tipo_cliente')
    nome = models.CharField(max_length=20)
    data_nascimento = models.DateField()

    class Meta:
        managed = False
        db_table = 'clientes'
        unique_together = (('id_cliente', 'i_tipo_cliente'),)


class Compras(models.Model):
    cliente = models.CharField(max_length=255)
    ingresso = models.IntegerField()
    lanche = models.IntegerField()
    valor_total = models.DecimalField(max_digits=10, decimal_places=2)
    data_compra = models.DateField()

    class Meta:
        managed = False
        db_table = 'compras'


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


class Filme(models.Model):
    id = models.IntegerField(primary_key=True)
    titulo = models.TextField()
    duracao = models.IntegerField()
    data_lancamento = models.DateField()
    diretor = models.TextField()
    genero_filme = models.TextField()

    class Meta:
        managed = False
        db_table = 'filme'


class Ingressos(models.Model):
    id = models.IntegerField(primary_key=True)
    tipo_tingresso = models.ForeignKey('Tipoingresso', models.DO_NOTHING, db_column='tipo_tIngresso')  # Field name made lowercase.
    sessao_id_ingresso = models.ForeignKey('Secoes', models.DO_NOTHING, db_column='sessao_id_ingresso')
    cliente_id_ingresso = models.ForeignKey(Clientes, models.DO_NOTHING, db_column='cliente_id_ingresso')
    assento_ingresso = models.IntegerField(unique=True)
    preco_ingresso = models.DecimalField(max_digits=10, decimal_places=0)

    class Meta:
        managed = False
        db_table = 'ingressos'


class ItensPedido(models.Model):
    id = models.IntegerField(primary_key=True)
    pedido = models.ForeignKey('Pedidos', models.DO_NOTHING)
    produto = models.ForeignKey('Produtos', models.DO_NOTHING)
    quantidade = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'itens_pedido'


class OfertasCinema(models.Model):
    id = models.IntegerField(primary_key=True)
    titulo = models.TextField()
    id_filme = models.IntegerField(blank=True, null=True)
    descricao = models.TextField(blank=True, null=True)
    valor = models.DecimalField(max_digits=10, decimal_places=0)
    data_inicio = models.DateField()
    data_fim = models.DateField()

    class Meta:
        managed = False
        db_table = 'ofertas_cinema'


class Pedidos(models.Model):
    id = models.IntegerField(primary_key=True)
    cliente = models.ForeignKey(Clientes, models.DO_NOTHING)
    data = models.DateField()

    class Meta:
        managed = False
        db_table = 'pedidos'


class Produtos(models.Model):
    id = models.IntegerField(primary_key=True)
    nome = models.CharField(max_length=255)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    tipo = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'produtos'


class Salas(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.TextField()
    capacidade = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'salas'


class Secoes(models.Model):
    id = models.IntegerField(primary_key=True)
    filme_id_secoes = models.ForeignKey(Filme, models.DO_NOTHING, db_column='filme_id_secoes')
    sala_id_secoes = models.ForeignKey(Salas, models.DO_NOTHING, db_column='sala_id_secoes')
    hora_inicio = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'secoes'


class Tipocliente(models.Model):
    id_tipocliente = models.IntegerField(primary_key=True)
    descricao = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tipocliente'


class Tipoingresso(models.Model):
    id_tipoingresso = models.IntegerField(db_column='id_tipoIngresso', primary_key=True)  # Field name made lowercase.
    descricao = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tipoingresso'
