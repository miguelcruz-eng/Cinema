# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from enum import unique
from django.db import models
from django.conf import settings
from django.utils import timezone
from django.core.mail import send_mail
from django.core.validators import RegexValidator
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models


class Atores(models.Model):
    i_id_atoresfilme = models.IntegerField(db_column='i_id_atoresFilme', primary_key=True)  # Field name made lowercase.
    s_nome_ator = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'atores'

    def __str__(self):
        return self.s_nome_ator


class Bilheteria(models.Model):
    formapagamento = models.IntegerField(db_column='FormaPagamento')  # Field name made lowercase.
    cliente_id_bilhe = models.OneToOneField('Cliente', models.DO_NOTHING, related_name='cliente_id_bilhe', primary_key=True)
    mostra_ofertas = models.IntegerField()
    comprar_i_ingresso_comprar = models.ForeignKey('Comprar', models.DO_NOTHING, related_name='comprar_i_ingresso_comprar')
    comprar_i_lanches_comprar = models.ForeignKey('Comprar', models.DO_NOTHING, related_name='comprar_i_lanches_comprar', to_field='i_lanches_comprar')
    comprar_i_estreia_comprar = models.ForeignKey('Comprar', models.DO_NOTHING, related_name='comprar_i_estreia_comprar', to_field='i_estreia_comprar')
    comprar_i_bilhe_field = models.ForeignKey('Comprar', models.DO_NOTHING, related_name='comprar_i_bilhe_field', to_field='i_bilhe_field')  # Field renamed because it ended with '_'.

    class Meta:
        managed = False
        db_table = 'bilheteria'
        unique_together = (('cliente_id_bilhe', 'mostra_ofertas'),)


class Cliente(models.Model):
    i_id_cliente = models.IntegerField(primary_key=True)
    s_nome_cliente = models.CharField(max_length=15)
    d_datanas_cliente = models.DateField(db_column='d_dataNas_cliente')  # Field name made lowercase.
    i_tipo_cliente = models.ForeignKey('Tipocliente', models.DO_NOTHING, db_column='i_tipo_cliente')

    class Meta:
        managed = False
        db_table = 'cliente'


class Comprar(models.Model):
    i_ingresso_comprar = models.OneToOneField('Ingressos', models.DO_NOTHING, db_column='i_ingresso_comprar', primary_key=True)
    i_lanches_comprar = models.ForeignKey('Lanches', models.DO_NOTHING, unique=True, related_name='i_lanches_comprar')
    i_estreia_comprar = models.ForeignKey('Estreias', models.DO_NOTHING, unique=True, related_name='i_estreia_comprar')
    i_bilhe_field = models.ForeignKey('Bilheteria', models.DO_NOTHING, unique=True, db_column='i_bilhe_field')  # Field renamed because it ended with '_'.

    class Meta:
        managed = False
        db_table = 'comprar'
        unique_together = (('i_ingresso_comprar', 'i_lanches_comprar', 'i_estreia_comprar', 'i_bilhe_field'),)


class Estreias(models.Model):
    i_idestreia_est = models.IntegerField(db_column='i_idEstreia_est', primary_key=True)  # Field name made lowercase.
    d_dataestreia_est = models.DateField(db_column='d_dataEstreia_est')  # Field name made lowercase.
    ingressos_i_cod_ingresso = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'estreias'
        unique_together = (('i_idestreia_est', 'ingressos_i_cod_ingresso'),)


class Filme(models.Model):
    i_id_filme = models.IntegerField(primary_key=True)
    s_titulo_filme = models.CharField(max_length=30)
    s_nacionalidade_filme = models.CharField(max_length=10)
    s_estudio_filme = models.CharField(max_length=10)
    i_tipofilme_filme = models.ForeignKey('Tipofilme', models.DO_NOTHING, db_column='i_tipoFilme_filme')  # Field name made lowercase.
    i_id_atores = models.ForeignKey(Atores, models.DO_NOTHING, db_column='i_id_atores')

    class Meta:
        managed = False
        db_table = 'filme'
        unique_together = (('i_id_filme', 'i_id_atores'),)
    
    def __str__(self):
        return self.s_titulo_filme


class Ingressos(models.Model):
    i_cod_ingresso = models.IntegerField(primary_key=True)
    f_preco_ingresso = models.IntegerField()
    secoes_i_cod_secoes = models.ForeignKey('Secoes', models.DO_NOTHING, related_name='secoes_i_cod_secoes')
    i_id_estreia = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'ingressos'


class Lanches(models.Model):
    i_cod_lanche = models.IntegerField(primary_key=True)
    f_preco_lanche = models.FloatField()
    i_quantidade_lanche = models.IntegerField()
    i_tipo_lanche = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'lanches'


class Ofertas(models.Model):
    i_id_ofertas = models.IntegerField()
    ofertas = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'ofertas'


class Sala(models.Model):
    i_cod_sala = models.IntegerField(primary_key=True)
    i_capa_sala = models.IntegerField()
    i_poltrona_sala = models.IntegerField()
    i_numero_sala = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'sala'


class Secoes(models.Model):
    i_cod_secoes = models.IntegerField(primary_key=True)
    d_data_secoes = models.DateField()
    h_hora_secoes = models.DateTimeField()
    i_tiposala_secoes = models.ForeignKey(Sala, models.DO_NOTHING, related_name='i_TipoSala_secoes')  # Field name made lowercase.
    filme_i_id_filme = models.ForeignKey(Filme, models.DO_NOTHING, related_name='filme_i_id_filme')

    class Meta:
        managed = False
        db_table = 'secoes'
        unique_together = (('i_cod_secoes', 'filme_i_id_filme'),)


class Tipocliente(models.Model):
    i_id_tcliente = models.IntegerField(db_column='i_id_TCliente', primary_key=True)  # Field name made lowercase.
    s_desc_tcliente = models.CharField(db_column='s_desc_TCliente', max_length=15, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tipocliente'

    def __str__(self):
        return self.s_desc_tcliente


class Tipofilme(models.Model):
    i_idcategoria_tipofilme = models.IntegerField(db_column='i_idCategoria_TipoFilme', primary_key=True)  # Field name made lowercase.
    s_genero_tipofilme = models.CharField(db_column='s_genero_TipoFilme', max_length=5)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tipofilme'
    
    def __str__(self):
        return self.s_genero_tipofilme
