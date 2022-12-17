# Generated by Django 4.1.4 on 2022-12-17 02:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cinema', '0015_ator_clientes_itenspedido_ofertascinema_pedidos_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Compras',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cliente', models.CharField(max_length=255)),
                ('ingresso', models.IntegerField()),
                ('lanche', models.IntegerField()),
                ('valor_total', models.DecimalField(decimal_places=2, max_digits=10)),
                ('data_compra', models.DateField()),
            ],
            options={
                'db_table': 'compras',
                'managed': False,
            },
        ),
    ]
