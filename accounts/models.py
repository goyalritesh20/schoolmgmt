from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    pass

    def is_student(self):
        return bool(getattr(self, "student", None))

    def is_teacher(self):
        return bool(getattr(self, "teacher", None))


class Student(User):
    fees = models.IntegerField()
    teachers = models.ManyToManyField('Teacher', related_name='students')

    class Meta:
        verbose_name = 'student'
        verbose_name_plural = 'students'


class Teacher(User):
    salary = models.IntegerField()
    subjects = models.ManyToManyField('Subject', related_name='teachers', blank=True)

    class Meta:
        verbose_name = 'teacher'
        verbose_name_plural = 'teachers'


class Subject(models.Model):
    name =  models.CharField(max_length=64)

    def __str__(self):
        return self.name