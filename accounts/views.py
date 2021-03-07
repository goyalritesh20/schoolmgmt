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
from accounts.permissions import StudentOnlyPermission

# Create your views here.

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