from django.contrib import admin
from .models import User, Sale, Student, Video, Payment, Teacher, Course
# Register your models here.

admin.site.register(User)
admin.site.register(Student)
admin.site.register(Video)
admin.site.register(Sale)
admin.site.register(Payment)
admin.site.register(Teacher)
admin.site.register(Course)