# Generated by Django 2.2.13 on 2020-10-11 22:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('requests', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Requests',
            new_name='Request',
        ),
    ]
