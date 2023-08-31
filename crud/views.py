from django.shortcuts import render
from .serializer import Studentserilaiser
from .models import Student
from rest_framework.response import Response
from rest_framework.generics import ListAPIView
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.throttling import AnonRateThrottle,UserRateThrottle




class Student_view(ListAPIView):
    queryset = Student.objects.all()
    serializer_class = Studentserilaiser
    
    def get_queryset(self):
        user = self.request.user
        return Student.objects.filter(passby=user)
    

    

    
    


        


        




# Create your views here.
