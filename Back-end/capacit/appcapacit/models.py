from django.db import models

# Create your models here.
class User(models.Model):
    id_user = models.AutoField(primary_key=True)
    first_name = models.CharField (max_length=45)
    last_name = models.CharField (max_length=45)
    username = models.CharField (max_length=45)
    email = models.EmailField()
    password = models.CharField (max_length=32)
    activate = models.BooleanField()    
    role = models.CharField(max_length=45)
    create_time= models.DateTimeField (auto_now_add=True)
    user_git = models.CharField (max_length=45)
    user_linkedin = models.CharField (max_length=100)

class Student(models.Model):
    id_student = models.AutoField(primary_key=True)  
    id_user = models.ForeignKey()
    dni = models.IntegerField()
    user_vip = models.BooleanField()

class Video(models.Model):
    id_video = models.AutoField(primary_key=True)
    descripcion = models.TextField (max_length=500)
    blob = models.TextField ()
    id_course = models. ForeignKey ()
    id_teacher = models.ForeignKey()
    link = models.CharField ( max_length=45)
    


