from django.shortcuts import render
from django.views import View
from rest_framework import viewsets
from .models import Students, Video_1
from .serializers import StudentsSerializer, StudentsForm, VideoSerializer, VideoUploadForm # You need to create a serializer for your model
from django.shortcuts import render, get_object_or_404, redirect
from django.http import FileResponse, JsonResponse
import json
from rest_framework.parsers import FileUploadParser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.parsers import MultiPartParser
from django.http import FileResponse, StreamingHttpResponse


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


def upload_video(request):
    if request.method == 'POST':
        form = VideoUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('video-list')  # Redirect to video list after successful upload
    else:
        form = VideoUploadForm()
    return render(request, 'myApp/upload_video.html', {'form': form})

def video_list(request):
    videos = Video_1.objects.all()
    return render(request, 'myApp/video_list.html', {'videos': videos})

class VideoWatchView(View):
    def get(self, request, pk):
        video = get_object_or_404(Video_1, pk=pk)
        video_file = video.vid
        response = FileResponse(video_file.open('rb'))
        response['Content-Disposition'] = f'attachment; filename="{video_file.name}"'
        return response

def stream_video(request, pk):
    video = get_object_or_404(Video_1, pk=pk)
    video_file = video.vid
    chunk_size = 8192  # You can adjust the chunk size as needed

    def file_iterator(file_path, chunk_size):
        with open(file_path, 'rb') as f:
            while True:
                chunk = f.read(chunk_size)
                if not chunk:
                    break
                yield chunk

    response = StreamingHttpResponse(file_iterator(video_file.path, chunk_size), content_type='video/mp4')
    response['Content-Disposition'] = f'inline; filename="{video_file.name}"'
    return response
