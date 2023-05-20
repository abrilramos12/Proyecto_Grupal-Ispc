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
    id_user = models.ForeignKey(User, to_field="id_user")
    dni = models.IntegerField()
    user_vip = models.BooleanField()

class Video(models.Model):
    id_video = models.AutoField(primary_key=True)
    descripcion = models.TextField (max_length=500)
    blob = models.TextField ()
    id_course = models. ForeignKey ()
    id_teacher = models.ForeignKey()
    link = models.CharField ( max_length=45)

class Sale(models.Model):
    id_sale = models.AutoField(primary_key=True)
    state = models.CharField(max_length= 50, null=True, help_text="Ingrese el estado de la compra" )
    discount = models.FloatField(help_text="Descuento")
    value = models.FloatField(null=False)
    id_student = models.ForeignKey("Student", on_delete=models.CASCADE)
    id_course = models.ForeignKey("Course", on_delete=models.CASCADE)
    id_teacher = models.ForeignKey("Teacher", on_delete=models.CASCADE)


class Payment(models.Model):
    id_payment = models.AutoField(primary_key=True)
    date = models.DateField(null=False, auto_now_add=True)
    total = models.FloatField(null=False)
    id_sale = models.ForeignKey("Sale", on_delete=models.CASCADE)


