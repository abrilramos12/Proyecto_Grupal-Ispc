from rest_framework import serializers

from appcapacit.models import User, Course

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id_user", "first_name", "last_name", "username", "email", "password", "activate", "role", "create_time", "user_git", "user:linkedin")

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ("id_course", "name", "languaje", "tag_1", "tag_2", "link", "id_teacher")
        
