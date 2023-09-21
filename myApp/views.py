from django.shortcuts import render
from rest_framework import viewsets
from .models import Students
from .serializers import StudentsSerializer, StudentsForm # You need to create a serializer for your model
from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
import json


class StudentsViewSet(viewsets.ModelViewSet):
    queryset = Students.objects.all()
    serializer_class = StudentsSerializer

def Students_list(request):
    people = Students.objects.all()
    return render(request, "myapp/Students_list.html", {"people": people})

def Students_detail(request, pk):
    St = get_object_or_404(Students, pk=pk)
    return render(request, "myapp/Students_detail.html", {"St": St})

def create_Students(request):
    if request.method == "POST":
        form = StudentsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("Students_list")
    else:
        form = StudentsForm()
    return render(request, "myapp/create_Students.html", {"form": form})

def update_Students(request, pk):
    St = get_object_or_404(Students, pk=pk)
    if request.method == "POST":
        form = StudentsForm(request.POST, instance=St)  # Use instance=St here
        if form.is_valid():
            form.save()
            return redirect("Students_list")
    else:
        form = StudentsForm(instance=St)
    return render(request, "myapp/update_Students.html", {"form": form, "St": St})

def delete_Students(request, pk):
    St = get_object_or_404(Students, pk=pk)
    if request.method == "POST":
        Students.delete()
        return redirect("Students_list")
    return render(request, "myapp/delete_Students.html", {"St": St})

def api_get_Students(request, pk):
    St = get_object_or_404(Students, pk=pk)
    data = {
        "name": St.name,
        "age": St.age,
        "city": St.city,
    }
    return JsonResponse(data)

def api_create_Students(request):
    if request.method == "POST":
        data = json.loads(request.body)
        form = StudentsForm(data)
        if form.is_valid():
            Students = form.save()
            data = {
                "message": "Students created successfully",
                "id": Students.pk,
            }
            return JsonResponse(data, status=201)
        else:
            data = {
                "error": "Invalid data",
            }
            return JsonResponse(data, status=400)
