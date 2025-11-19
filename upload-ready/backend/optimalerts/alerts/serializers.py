from rest_framework import serializers
from .models import Alert, Employee

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = ("id", "name")

class AlertSerializer(serializers.ModelSerializer):
    employee = EmployeeSerializer(read_only=True) #source="employee", read_only=True)
    class Meta:
        model = Alert
        fields = ("id", "employee", "severity", "category", "created_at", "status")