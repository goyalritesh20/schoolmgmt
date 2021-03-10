from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
User = get_user_model()
from rest_framework.views import APIView
from django.http import HttpResponse, JsonResponse, Http404
from rest_framework import status
from rest_framework.response import Response
from accounts.models import Student, Teacher, Subject
from accounts import serializers
from rest_framework import permissions
from accounts.permissions import StudentOnlyPermission, TeacherOnlyPermission
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def home_view(request):
    if not request.user.is_superuser:
        return HttpResponse('Only Admin has access to view this page.')

    students = Student.objects.all()

    student_subjects = []
    for student in students:
        subnames = []
        teachers = student.teachers.all()
        for teacher in teachers:
            subjects = teacher.subjects.all()
            subnames += [sub.name for sub in subjects]
        subnames = list(set(subnames))
        student_subjects.append( (student, teachers, subnames) )

    ctx = {'students_data': student_subjects }
    return render(request,'report.html',ctx)


class StudentDetailAPI(APIView):

    permission_classes = [permissions.IsAuthenticated, StudentOnlyPermission]

    def get_object(self, pk):
        try:
            return Student.objects.get(pk=pk)
        except Student.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        student = self.get_object(pk)
        serializer = serializers.StudentSerializer(student)
        return Response(serializer.data)


class TeacherDetailAPI(APIView):

    permission_classes = [permissions.IsAuthenticated, TeacherOnlyPermission]

    def get_object(self, pk):
        try:
            return Teacher.objects.get(pk=pk)
        except Teacher.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        teacher = self.get_object(pk)
        serializer = serializers.TeacherSerializer(teacher)
        return Response(serializer.data)

    
    def patch(self, request, pk, format=None):
        teacher = self.get_object(pk)
        serializer = serializers.TeacherUpdateSerializer(teacher, data=request.data, partial=True)
        if serializer.is_valid():
            teacher = serializer.save()
            serializer = serializers.TeacherSerializer(teacher)
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
