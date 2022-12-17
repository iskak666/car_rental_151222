from django.db import models
from django.contrib.auth.models import User
from datetime import date, datetime


class Station(models.Model):

    towns = (
        ('Tokmok', 'Tokmok'),
        ('Balykchi', 'Balykchi'),
        ('Kant', 'Kant'),
        ('Cholpon-Ata', 'Cholpon-Ata'),
        ('Ala-Archa', 'Ala-Archa'),
        ('Manas', 'Manas'),
        ('Ivanovka', 'Ivanovka'),
        ('Sverdlovski','Sverdlovski'),
        ('Oktyabrski','Oktyabrski'),
        ('Pervomaiski','Pervomaiski'),
        ('Ak-Orgo','Ak-Orgo'),
        ('Lebedinovka','Lebedinovka'),
        ('Prigorodnoe','Prigorodnoe'),
        ('Leninski','Leninski'),
        ('Tunguch','Tunguch'),
    )

    counties = (
        ('Yssyk-Kol', 'Yssyk-Kol'),
        ('Bishkek', 'Bishkek'),
        ('Chui', 'Chui'),
    )

    name = models.CharField(max_length=100)
    county = models.CharField(
        max_length=100, choices=counties, default='Chui')
    town = models.CharField(max_length=100, choices=towns, default='Tokmok')
    mobile = models.CharField(max_length=10, unique=True)
    manager = models.ForeignKey(User, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.name


class Car(models.Model):
    Reg_No = models.CharField(max_length=10, unique=True)
    name = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    image = models.ImageField(upload_to='cars/%Y/%m/%d')
    available = models.BooleanField(default=True)
    fee = models.DecimalField(max_digits=10, decimal_places=2)
    fine_rate = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()

    def __str__(self):
        return self.name


class Reservation(models.Model):

    car = models.ForeignKey(Car, on_delete=models.DO_NOTHING)
    station = models.ForeignKey(Station, on_delete=models.DO_NOTHING)
    pick_date = models.DateField(auto_now_add=True)
    return_date = models.DateField()
    has_paid = models.BooleanField(default=False)
    has_returned = models.BooleanField(default=False)
    customer = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    customer_phone = models.CharField(max_length=10)
    id_number = models.CharField(max_length=9, unique=True)

    @ property
    def duration(self):
        total_days = (self.return_date-self.pick_date).days
        return total_days

    @ property
    def is_overdue(self):
        return date.today() > self.return_date

    @ property
    def overdue_by(self):
        total_days = (date.today() - self.return_date).days
        return total_days

    @ property
    def fine(self):
        fined = self.car.fine_rate * self.overdue_by
        return fined


class Contact(models.Model):
    customer = models.CharField(max_length=100)
    email = models.CharField(max_length=200)
    message = models.TextField()

    def __str__(self):
        return self.customer
