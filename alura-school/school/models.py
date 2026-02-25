from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(blank=False, unique=True)
    cpf = models.CharField(max_length=11, unique=True)
    birth_date = models.DateField()
    phone_number = models.CharField(max_length=14)

    def __str__(self):
        return self.name
    
class Course(models.Model):
    LEVEL = (
        ('B', 'Beginner'),
        ('I', 'Intermediate'),
        ('A', 'Advanced'),
    )
    code = models.CharField(max_length=10, unique=True)
    description = models.TextField(blank=False)
    level = models.CharField(max_length=1, choices=LEVEL, blank=False, default='B')

    def __str__(self):
        return self.code