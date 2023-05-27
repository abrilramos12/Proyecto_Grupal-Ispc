from django.shortcuts import render

from rest_framework import generics
from appcapacit.models import User, Course
from appcapacit.serializers import UserSerializer, CourseSerializer

from django.contrib.auth import authenticate, login, logout
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

    

# Create your views here.

class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class CourseList(generics.ListCreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

class CourseDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer



class LoginView(APIView):
    def post(self, request):
        # recuperamos las credenciales y autenticamos al usuario
        email = request.data.get("email", None)
        password = request.data.get("password", None)
        user = authenticate(email=email, password=password)

        #Si es correcto añadimos a la request la información de sesión
        if user: 
            login(request, user)
            return Response(
                status=status.HTTP_200_OK)
        
        #Si NO es correcto devolvemos un error en la petición
        return Response(
            status=status.HTTP_404_NOT_FOUND)
    
class LogoutView(APIView):
    def post(self, request):
        # borramos de la request la información de sesion
        logout(request)

        #devolvemos la respuesta al cliente
        return Response(
            status=status.HTTP_200_OK)    

        



