from rest_framework import serializers
from .models import Students
# myapp/forms.py
from django import forms


class StudentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Students
        fields = '__all__'


class StudentsForm(forms.ModelForm):
    class Meta:
        model = Students
        fields = ["name", "age", "city"]

