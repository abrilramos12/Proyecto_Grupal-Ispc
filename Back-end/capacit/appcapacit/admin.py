from django.contrib import admin
from .models import User, Sale, Student, Video, Payment, Teacher, Course

from django.contrib import admin
from .models import CustomUser
from django.contrib.auth import get_user_model 

# Register your models here.

admin.site.register(User)
admin.site.register(Student)
admin.site.register(Video)
admin.site.register(Sale)
admin.site.register(Payment)
admin.site.register(Teacher)
admin.site.register(Course)

@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    pass