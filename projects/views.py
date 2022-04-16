from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework import viewsets
from rest_framework.response import Response
from projects import models
# Create your views here.

from rest_framework import generics
from .serializers import EmployeeSerializer, ProjectSerializer
from .models import Employee, Project


class ListEmployee(generics.ListAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer


list_employee = ListEmployee.as_view()

class ListProjects(generics.ListAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


list_projects = ListProjects.as_view()

class AddProject(generics.CreateAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


add_projects = AddProject.as_view()



@api_view(
    ["GET"],
)
def get_project_status(request):
    return Response(
        [
            {"value": models.ONGOING_STATUS, "text": "Ongoing"},
            {"value": models.ENDED_STATUS, "text": "Ended"},
            {"value": models.COMING_STATUS, "text": "Coming"},
        ]
    )

