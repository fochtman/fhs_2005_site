from django.contrib.auth.models import User
from django.db import models

class FHSUser(models.Model):
    user = models.OneToOneField(User)
    is_married = models.BooleanField(default=False)
    ticket_num = models.IntegerField(default=0)
    current_city = models.CharField(max_length=50)
    current_state = models.CharField(max_length=50)
