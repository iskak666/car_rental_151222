# Generated by Django 2.2.5 on 2020-08-15 15:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0009_contacts'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Contacts',
            new_name='Contact',
        ),
    ]