from django.db import models
from accounts.models import Professor, Student
from django.utils import timezone
# Create your models here.


class Task(models.Model):
    title = models.CharField(max_length=400)
    description = models.TextField()
    professor = models.ForeignKey(Professor, on_delete=models.CASCADE)
    deadline = models.CharField(max_length=30)
    student = models.ForeignKey(Student, on_delete=models.CASCADE, null=True, blank=True)
    file = models.FileField(upload_to="tasks", null=True, blank=True)
    delivary_date = models.DateTimeField(max_length=200, null=True, blank=True)
