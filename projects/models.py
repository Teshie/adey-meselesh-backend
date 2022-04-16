from django.db import models
from django.db import models
# Create your models here.


COMING_STATUS = "Coming"
ONGOING_STATUS = "Ongoing"
ENDED_STATUS = "Ended"

PROJECT_STATUS_CHOICES = (
    (COMING_STATUS, "Coming"),
    (ONGOING_STATUS, "Ongoing"),
    (ENDED_STATUS, "Ended"),
)
class Employee(models.Model):
    employee_name =  models.CharField(max_length=255)
    def __str__(self):
        return self.employee_name
    
class Project(models.Model):
    project_name = models.CharField(max_length=255, blank=False)
    created_by = models.ForeignKey(
        Employee, related_name='employee', on_delete=models.DO_NOTHING, null=True) 
    status = models.CharField(
        max_length=50, choices=PROJECT_STATUS_CHOICES, default=COMING_STATUS, null=True, blank=True
    )
    start_date = models.DateField( null=True)
    end_date = models.DateField( null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.project_name

