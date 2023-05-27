from rest_framework import serializers
from appcapacit.models import User, Course

from django.contrib.auth import get_user_model



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id_user", "first_name", "last_name", "username", "email", "password", "activate", "role", "create_time", "user_git", "user:linkedin")

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ("id_course", "name", "languaje", "tag_1", "tag_2", "link", "id_teacher")
        



class UserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required = True)
    username = serializers.CharField(required=True)
    password = serializers.CharField(min_length=8)

    class Meta:
        model = get_user_model ()
        fields = ("email", "username", "password")

