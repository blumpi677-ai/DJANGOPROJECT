from django.db import models
from accounts.models import User

class Job(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    salary = models.IntegerField()
    location = models.CharField(max_length=255)
    category = models.CharField(max_length=100)
    employer = models.ForeignKey(User, on_delete=models.CASCADE)
    jd_file = models.FileField(upload_to='job_descriptions/', null=True, blank=True)