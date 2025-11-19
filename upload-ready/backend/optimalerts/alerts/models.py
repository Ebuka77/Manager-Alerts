from django.db import models

# Create your models here.
class Employee(models.Model):
    id = models.CharField(max_length=32, primary_key=True)
    name = models.CharField(max_length=200)
    reports_to = models.CharField(max_length=32, null=True, blank=True)

    def __str__(self):
        return self.name

class Alert(models.Model):
    STATUS_CHOICES = (("open","open"),("dismissed","dismissed"))
    SEVERITY_CHOICES = (("low","low"),("medium","medium"),("high","high"))

    id = models.CharField(max_length=32, primary_key=True)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name="alerts")
    severity = models.CharField(max_length=10, choices=SEVERITY_CHOICES)
    category = models.CharField(max_length=100)
    created_at = models.DateTimeField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default="open")

    def __str__(self):
        return self.message
