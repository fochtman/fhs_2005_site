from django.contrib.auth.models import User
from django.db import models

class FHSUser(models.Model):
    user = models.OneToOneField(User, primary_key=True)
    is_married = models.BooleanField(default=False)
    num_kids = models.IntegerField(default=0)
    num_ticket = models.IntegerField(default=0)
    profession = models.CharField(max_length=50)
    current_city = models.CharField(max_length=50)
    current_state = models.CharField(max_length=50)

    def __unicode__(self):
        return '{0}, {1}'.format(self.user.last_name, self.user.first_name)


class Image(models.Model):
    image = models.ImageField(upload_to='images')
