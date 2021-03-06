from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    pass


class Student(User):
    fees = models.IntegerField()
    teachers = models.ManyToManyField('Teacher', related_name='students')

    class Meta:
        verbose_name = 'student'
        verbose_name_plural = 'students'


class Teacher(User):
    salary = models.IntegerField()

    class Meta:
        verbose_name = 'teacher'
        verbose_name_plural = 'teachers'



class Subject(models.Model):
    name =  models.CharField(max_length=64)
    students = models.ManyToManyField('Student', related_name='subjects')
    teachers = models.ManyToManyField('Teacher', related_name='subjects')

    def __str__(self):
        return self.name