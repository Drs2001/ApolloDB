from django.db import models
from django.contrib.auth.models import User

class Application(models.Model):
    user = models.ForeignKey(
        User, 
        on_delete=models.CASCADE
    )
    company_name = models.CharField(max_length=255)
    url = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    position = models.CharField(max_length=255)
    followed_up = models.BooleanField(default=False)
    application_date = models.DateField()

