# Create your models here.
from django.db import models

class Classroom(models.Model):
    name = models.CharField(max_length=200)
    teacher_name = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return f"{self.name} ({self.teacher_name})"

class Student(models.Model):
    name = models.CharField(max_length=200)
    age = models.PositiveIntegerField()
    classroom = models.ForeignKey(Classroom, on_delete=models.CASCADE, related_name='students')

    def __str__(self):
        return self.name