from django.db import models
from django.contrib.auth.models import User


class UserInfo(models.Model):
    user = models.OneToOneField(User)
    def __str__(self):
        return (self.user)
    
    def get_data(self,field):
        return  getattr(self,field)

class UserTextData(models.Model):
    user = models.OneToOneField(User,unique = 'TRUE')
    text = models.CharField(max_length=1000)

    def __str__(self):
        return (self.user.username)

    def get_data(self,field):
        return  getattr(self,field)

class UserImageData(models.Model):
    user = models.OneToOneField(User)
    image = models.ImageField(upload_to='saved_pics/')

    def __str__(self):
        return (self.user)

