from rest_framework import serializers
from .models import Employee, Project

class EmployeeSerializer(serializers.ModelSerializer):
    created_by = serializers.RelatedField( read_only=True)
    class Meta:
        fields = '__all__'
        model = Employee


class ProjectSerializer(serializers.ModelSerializer):
    created_by = serializers.CharField(source="created_by.employee_name", read_only=True)

    class Meta:
        fields = '__all__'
        model = Project