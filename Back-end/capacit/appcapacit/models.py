from django.db import models

# Create your models here.
class User(models.Model):
    id_user = models.CharField (max_length=256)
    first_name = models.CharField (max_length=45)
    last_name = models.CharField (max_length=45)
    username = models.CharField (max_length=16)
    email = models.CharField (max_length=256)
    password = models.CharField (max_length=32)
    role = models.CharField(max_length=45)
    reate_time= models.DateTimeField (auto_now_add=True)
    user_git = models.CharField (max_length=128)
    user_linkedin = models.CharField (max_length=128)

