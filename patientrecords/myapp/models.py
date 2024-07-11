
from django.db import models

class Patient(models.Model):
    GENDER_CHOICES = (
        ('male', 'Male'),
        ('female', 'Female'),
        ('other', 'Other'),
    )

    name = models.CharField(max_length=100)
    address = models.TextField()
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    age = models.PositiveIntegerField()
    dob = models.DateField()
    weight = models.CharField(max_length=10)
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    prescription = models.TextField(blank=True, null=True)
    observation = models.TextField(blank=True, null=True)