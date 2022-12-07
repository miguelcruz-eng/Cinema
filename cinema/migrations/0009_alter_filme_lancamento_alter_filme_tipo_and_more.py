# Generated by Django 4.1.4 on 2022-12-06 23:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cinema', '0008_alter_filme_tipo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='filme',
            name='lancamento',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='filme',
            name='tipo',
            field=models.CharField(choices=[('cartaz', 'Cartaz'), ('preestreia', 'Pre-Estreia')], max_length=10),
        ),
        migrations.AlterField(
            model_name='lanche',
            name='tipo',
            field=models.CharField(choices=[('acompanhamento', 'Acompanhamento'), ('bebida', 'Bebida'), ('refeicao', 'Refeicao')], max_length=15),
        ),
    ]