# Generated by Django 2.2.5 on 2020-08-15 15:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0010_auto_20200815_1808'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservation',
            name='id_number',
            field=models.CharField(max_length=9, unique=True),
        ),
    ]
