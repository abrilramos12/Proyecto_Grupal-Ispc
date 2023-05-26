from django.db import models
from datetime import datetime

# Create your models here.
class User(models.Model):
    id_user = models.AutoField(primary_key=True)
    first_name = models.CharField (max_length=45)
    last_name = models.CharField (max_length=45)
    username = models.CharField (max_length=45)
    email = models.EmailField()
    password = models.CharField (max_length=32)
    activate = models.BooleanField(default=False)    
    role = models.CharField(max_length=45)
    create_time= models.DateTimeField (auto_now_add=True)
    user_git = models.CharField (max_length=45)
    user_linkedin = models.CharField (max_length=100)

    # metodo str para que retorne nombre, no objet
    def __str__(self):
        return "{} {} {} {}".format(self.id_user, self.first_name, self.last_name, self.username)

class Student(models.Model):
    id_student = models.AutoField(primary_key=True)  
    id_user = models.ForeignKey(User, to_field="id_user", on_delete=models.CASCADE)
    dni = models.IntegerField()
    user_vip = models.BooleanField()

    def __str__(self):
        return "{} {}".format(self.id_student, self.dni)

class Video(models.Model):
    id_video = models.AutoField(primary_key=True)
    descripcion = models.TextField (max_length=500)
    blob = models.TextField ()
    id_course = models. ForeignKey ("Course", on_delete=models.CASCADE)
    id_teacher = models.ForeignKey("Teacher", on_delete=models.CASCADE)
    link = models.CharField ( max_length=45)

    def __str__(self):
        return "{} {}".format(self.id_video, self.id_course)

class Sale(models.Model):
    id_sale = models.AutoField(primary_key=True)
    state = models.CharField(max_length= 50, null=True, help_text="Ingrese el estado de la compra" )
    discount = models.FloatField(help_text="Descuento")
    value = models.FloatField(null=False)
    id_student = models.ForeignKey("Student", on_delete=models.CASCADE)
    id_course = models.ForeignKey("Course", on_delete=models.CASCADE)
    id_teacher = models.ForeignKey("Teacher", on_delete=models.CASCADE)

    def __str__(self):
        return "{}".format(self.id_sale)

class Payment(models.Model):
    id_payment = models.AutoField(primary_key=True)
    date = models.DateField(null=False, auto_now_add=True)
    total = models.FloatField(null=False)
    id_sale = models.ForeignKey("Sale", on_delete=models.CASCADE)

    def __str__(self):
        return "{} {}".format(self.id_payment, self.date)

class Teacher(models.Model):
    id_teacher = models.AutoField(primary_key=True)  
    id_user = models.ForeignKey(User, to_field="id_user", on_delete=models.CASCADE)
    dni = models.IntegerField()

    def __str__(self):
        return "{} {}".format(self.id_teacher, self.dni)

class Course(models.Model):
    id_course = models.AutoField(primary_key=True)
    name = models.CharField (max_length=45)
    languaje = models.CharField (max_length=45)
    tag_1 = models.CharField (max_length=45)
    tag_2 = models.CharField (max_length=45)
    link = models.CharField (max_length=45)
    id_teacher = models.ForeignKey("Teacher", on_delete=models.CASCADE)

    def __str__(self):
        return "{} {} {}".format(self.id_course, self.name, self.languaje)



