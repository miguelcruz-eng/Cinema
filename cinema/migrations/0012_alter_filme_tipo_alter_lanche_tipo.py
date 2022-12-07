# Generated by Django 4.1.4 on 2022-12-07 00:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cinema', '0011_alter_lanche_tipo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='filme',
            name='tipo',
            field=models.CharField(choices=[('preestreia', 'Pre-Estreia'), ('cartaz', 'Cartaz')], max_length=10),
        ),
        migrations.AlterField(
            model_name='lanche',
            name='tipo',
            field=models.CharField(choices=[('refeicao', 'Refeicao'), ('acompanhamento', 'Acompanhamento'), ('bebida', 'Bebida')], max_length=15),
        ),
    ]