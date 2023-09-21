from rest_framework import serializers
from .models import Students, Video_1
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



class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video_1
        fields = ['name', 'vid']


class VideoUploadForm(forms.ModelForm):
    class Meta:
        model = Video_1
        fields = ['name', 'vid']
