# Generated by Django 2.2.5 on 2020-08-12 11:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0007_auto_20200812_1357'),
    ]

    operations = [
        migrations.AlterField(
            model_name='station',
            name='county',
            field=models.CharField(choices=[('Mombasa', 'Mombasa'), ('Kwale', 'Kwale'), ('Kilifi', 'Kilifi'), ('Tana River', 'Tana River'), ('Lamu', 'Lamu'), ('Taita Taveta', 'Taita Taveta'), ('Garissa', 'Garissa'), ('Wajir', 'Wajir'), ('Mandera', 'Mandera'), ('Marsabit', 'Marsabit'), ('Isiolo', 'Isiolo'), ('Meru', 'Meru'), ('Tharaka Nithi', 'Tharaka Nithi'), ('Embu', 'Embu'), ('Kitui', 'Kitui'), ('Machakos', 'Machakos'), ('Makueni', 'Makueni'), ('Nyandarua', 'Nyandarua'), ('Nyeri', 'Nyeri'), ('Kirinyaga', 'Kirinyaga'), ("Murang'a", "Murang'a"), ('Kiambu', 'Kiambu'), ('Turkana', 'Turkana'), ('West Pokot', 'West Pokot'), ('Samburu', 'Samburu'), ('Trans-Nzoia', 'Trans-Nzoia'), ('Uasin Gishu', 'Uasin Gishu'), ('Elgeyo Marakwet', 'Elgeyo Marakwet'), ('Nandi', 'Nandi'), ('Baringo', 'Baringo'), ('Laikipia', 'Laikipia'), ('Nakuru', 'Nakuru'), ('Narok', 'Narok'), ('Kajiado', 'Kajiado'), ('Kericho', 'Kericho'), ('Bomet', 'Bomet'), ('Kakamega', 'Kakamega'), ('Vihiga', 'Vihiga'), ('Bungoma', 'Bungoma'), ('Busia', 'Busia'), ('Siaya', 'Siaya'), ('Kisumu', 'Kisumu'), ('Homa Bay', 'Homa Bay'), ('Migori', 'Migori'), ('Kisii', 'Kisii'), ('Nyamira', 'Nyamira'), ('Nairobi', 'Nairobi')], default='Nairobi', max_length=100),
        ),
    ]
