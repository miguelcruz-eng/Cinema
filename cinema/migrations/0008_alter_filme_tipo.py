# Generated by Django 4.1.3 on 2022-12-06 01:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cinema', '0007_rename_name_lanche_title_alter_filme_tipo_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='filme',
            name='tipo',
            field=models.CharField(choices=[('preestreia', 'Pre-Estreia'), ('cartaz', 'Cartaz')], max_length=10),
        ),
    ]
