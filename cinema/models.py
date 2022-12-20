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
    
    def __str__(self):
        return self.nome


class AtorFilme(models.Model):
    ator = models.OneToOneField(Ator, models.DO_NOTHING, primary_key=True)
    filme = models.ForeignKey('Filme', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'ator_filme'
        unique_together = (('ator', 'filme'),)

class Clientes(models.Model):
    id_cliente = models.IntegerField(primary_key=True)
    i_tipo_cliente = models.ForeignKey('Tipocliente', models.DO_NOTHING, db_column='i_tipo_cliente')
    nome = models.CharField(max_length=20)
    data_nascimento = models.DateField()

    class Meta:
        managed = False
        db_table = 'clientes'
        unique_together = (('id_cliente', 'i_tipo_cliente'),)
    
    def __str__(self):
        return self.nome

class Compras(models.Model):
    cliente = models.CharField(max_length=255)
    ingresso = models.IntegerField()
    lanche = models.IntegerField()
    valor_total = models.DecimalField(max_digits=10, decimal_places=2)
    data_compra = models.DateField()

    class Meta:
        managed = False
        db_table = 'compras'

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
    
    def __str__(self):
        return self.titulo


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

    def __str__(self):
        return self.nome


class Salas(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.TextField()
    capacidade = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'salas'
    
    def __str__(self):
        return self.name


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
    
    def __str__(self):
        return self.descricao


class Tipoingresso(models.Model):
    id_tipoingresso = models.IntegerField(db_column='id_tipoIngresso', primary_key=True)  # Field name made lowercase.
    descricao = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tipoingresso'

    def __str__(self):
        return self.descricao
