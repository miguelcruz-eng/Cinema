# Generated by Django 4.1.3 on 2022-12-06 01:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cinema', '0005_alter_filme_tipo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Lanche',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('tamanho', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('preco', models.FloatField()),
                ('foto', models.TextField()),
                ('tipo', models.CharField(choices=[('bebida', 'Bebida'), ('acompanhamento', 'Acompanhamento'), ('refeicao', 'Refeicao')], max_length=15)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]