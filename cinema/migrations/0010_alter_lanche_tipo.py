# Generated by Django 4.1.4 on 2022-12-06 23:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cinema', '0009_alter_filme_lancamento_alter_filme_tipo_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lanche',
            name='tipo',
            field=models.CharField(choices=[('acompanhamento', 'Acompanhamento'), ('refeicao', 'Refeicao'), ('bebida', 'Bebida')], max_length=15),
        ),
    ]
