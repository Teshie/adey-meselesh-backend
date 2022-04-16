from django.urls import path, include
from . import views
urlpatterns = [
    path("get-project-ststus", views.get_project_status, name="get_project_status"),   
    path("list-employee", views.list_employee, name="list_employee"),   
    path("list-projects", views.list_projects, name="get_projects"),   
    path("add-projects", views.add_projects, name="add_projects"),   
]
