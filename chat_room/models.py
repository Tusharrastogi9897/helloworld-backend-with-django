from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    username = models.CharField(max_length=20)
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=15)
    last_name = models.CharField(null=True, blank=True, max_length=15)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']
    
    @property
    def full_name(self):
        full_name = ""
        if self.first_name:
            full_name += self.first_name.lower()
        if self.last_name:
            full_name += "_{0}".format(self.last_name.lower())
        full_name += str(self.id)
        return full_name

class ChatRoom(AbstractBaseUser):
    room_name = models.CharField(max_length=20, unique=True)
    created_by = models.ForeignKey(User,related_name="%(class)s_created_by", on_delete=models.CASCADE,null=True, blank=True)
    created_on = models.DateTimeField(auto_now_add=True,null=True, blank=True)

    USERNAME_FIELD = 'room_name'
    REQUIRED_FIELDS = []
