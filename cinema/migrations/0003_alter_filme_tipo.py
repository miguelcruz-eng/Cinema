# Generated by Django 4.1.3 on 2022-12-05 22:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cinema', '0002_filme_foto_alter_filme_tipo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='filme',
            name='tipo',
            field=models.CharField(choices=[('estreia', 'Estreia'), ('preestreia', 'Pre-Estreia')], max_length=10),
        ),
    ]
