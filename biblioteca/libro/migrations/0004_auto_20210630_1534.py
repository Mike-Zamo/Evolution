# Generated by Django 3.2.4 on 2021-06-30 21:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libro', '0003_alter_libro_autor_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='autor',
            name='fecha_creacion',
            field=models.DateField(auto_now=True, verbose_name='Fecha de Creacion'),
        ),
        migrations.AddField(
            model_name='libro',
            name='fecha_creacion',
            field=models.DateField(auto_now=True, verbose_name='Fecha de Creacion'),
        ),
    ]