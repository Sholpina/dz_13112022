from django.db import models

# Create your models here.
from django.db import models


class Person(models.Model):
        name = models.CharField(max_length=100)
        age = models.IntegerField()

        # Add other fields relevant to a person

        def __str__(self):
                return self.name


class Child(models.Model):
        person = models.OneToOneField(Person, on_delete=models.CASCADE, primary_key=True)

        # Add fields specific to a child

        def __str__(self):
                return self.person.name


class IceCream(models.Model):
        flavor = models.CharField(max_length=50)

        # Add other fields related to an ice cream

        def __str__(self):
                return self.flavor


class IceCreamKiosk(models.Model):
        name = models.CharField(max_length=100)
        location = models.CharField(max_length=200)

        # Add other fields relevant to an ice cream kiosk

        def __str__(self):
                return self.name
