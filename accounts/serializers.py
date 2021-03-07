from rest_framework import serializers
from django.contrib.auth import get_user_model
User = get_user_model()
from accounts import models

class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Subject
        fields = ['name']


class TeacherSerializer(serializers.ModelSerializer):
    subjects = serializers.StringRelatedField(many=True)
    name = serializers.SerializerMethodField('get_first_name')  #name alias

    class Meta:
        model = models.Teacher
        fields = ['id', 'name', 'subjects',]
    
    def get_first_name(self, obj):
        return obj.first_name


class StudentSerializer(serializers.ModelSerializer):
    teachers = TeacherSerializer(many=True)
    student_name = serializers.SerializerMethodField('get_first_name')  #name alias

    class Meta:
        model = models.Student
        fields = ['id', 'username', 'student_name', 'teachers',]

    def get_first_name(self, obj):
        return obj.first_name
        