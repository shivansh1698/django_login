from django.db import models
from django.contrib.auth.models import User


class UserInfo(models.Model):
    user = models.OneToOneField(User)
    def __str__(self):
        return (self.email)
    
    def get_data(self,field):
        return  getattr(self,field)
