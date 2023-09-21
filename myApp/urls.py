from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import StudentsViewSet
from . import views

router = DefaultRouter()
router.register(r'students', StudentsViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path("student/", views.Students_list, name="Students_list"),
    path("student/<int:pk>/", views.Students_detail, name="Students_detail"),
    path("student/create/", views.create_Students, name="create_Students"),
    path("student/update/<int:pk>/", views.update_Students, name="update_Students"),
    path("student/delete/<int:pk>/", views.delete_Students, name="delete_Students"),
    path("api/student/<int:pk>/", views.api_get_Students, name="api_get_Students"),
    path("api/student/create/", views.api_create_Students, name="api_create_Students"),
]
