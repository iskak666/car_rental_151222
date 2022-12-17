# Generated by Django 2.2.5 on 2022-12-16 03:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0012_auto_20221213_1449'),
    ]

    operations = [
        migrations.AlterField(
            model_name='station',
            name='county',
            field=models.CharField(choices=[('Yssyk-Kol', 'Yssyk-Kol'), ('Bishkek', 'Bishkek'), ('Chui', 'Chui')], default='Nairobi', max_length=100),
        ),
        migrations.AlterField(
            model_name='station',
            name='town',
            field=models.CharField(choices=[('Tokmok', 'Tokmok'), ('Balykchi', 'Balykchi'), ('Kant', 'Kant'), ('Cholpon-Ata', 'Cholpon-Ata'), ('Ala-Archa', 'Ala-Archa'), ('Manas', 'Manas'), ('Ivanovka', 'Ivanovka'), ('Sverdlovski', 'Sverdlovski'), ('Oktyabrski', 'Oktyabrski'), ('Pervomaiski', 'Pervomaiski'), ('Ak-Orgo', 'Ak-Orgo'), ('Lebedinovka', 'Lebedinovka'), ('Prigorodnoe', 'Prigorodnoe'), ('Leninski', 'Leninski'), ('Tunguch', 'Tunguch')], default='Thika', max_length=100),
        ),
    ]
