from django.contrib.auth.models import User
from django.db import models

class FHSUser(models.Model):
    user = models.OneToOneField(User)
    is_married = models.BooleanField(default=False)
    num_kids = models.IntegerField(default=0)
    num_ticket = models.IntegerField(default=0)
    profession = models.CharField(max_length=50)
    current_city = models.CharField(max_length=50)
    current_state = models.CharField(max_length=50)
