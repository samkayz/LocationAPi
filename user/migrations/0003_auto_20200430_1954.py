# Generated by Django 3.0.5 on 2020-04-30 19:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_localgovernment_state'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='localgovernment',
            table='local_government',
        ),
    ]
