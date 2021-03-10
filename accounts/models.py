from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.core.exceptions import ValidationError

# Create your models here.

class User(AbstractUser):
    pass

    def is_student(self):
        return bool(getattr(self, "student", None))

    def is_teacher(self):
        return bool(getattr(self, "teacher", None))


class Student(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='student')
    fees = models.IntegerField()
    teachers = models.ManyToManyField('Teacher', related_name='students')

    def clean(self):
        if self.user.is_teacher():
            raise ValidationError('Teacher cannot be a student.')

    class Meta:
        verbose_name = 'student'
        verbose_name_plural = 'students'


class Teacher(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='teacher')
    salary = models.IntegerField()
    subjects = models.ManyToManyField('Subject', related_name='teachers', blank=True)

    def clean(self):
        if self.user.is_student():
            raise ValidationError('Student cannot be a teacher.')

    class Meta:
        verbose_name = 'teacher'
        verbose_name_plural = 'teachers'


class Subject(models.Model):
    name =  models.CharField(max_length=64)

    def __str__(self):
        return self.name