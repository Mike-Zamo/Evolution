# Generated by Django 3.2.4 on 2021-07-13 16:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libro', '0005_auto_20210630_1539'),
    ]

    operations = [
        migrations.AddField(
            model_name='autor',
            name='estado',
            field=models.BooleanField(default=True, verbose_name='Estado'),
        ),
    ]
