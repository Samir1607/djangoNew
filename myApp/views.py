from django.shortcuts import render
from rest_framework import viewsets
from .models import Students
from .serializers import StudentsSerializer  # You need to create a serializer for your model


class StudentsViewSet(viewsets.ModelViewSet):
    queryset = Students.objects.all()
    serializer_class = StudentsSerializer
