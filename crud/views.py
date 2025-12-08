from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.views import Response
from rest_framework.views import status
from .models import Students
from .serializers import studentSerializer

class studentList(APIView):
    def get(self,request):
        students=Students.objects.all()
        serializer=studentSerializer(students,many=True)
        return Response(serializer.data)

    def post(self,request):
        serializer=studentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
class studentDetail(APIView):
    def get(self,request,id):
        student=Students.objects.get(id=id)
        serializer=studentSerializer(student)
        return Response(serializer.data)
    
    def put(self,request,id):
        student=Students.objects.get(id=id)
        serializer=studentSerializer(student,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self,request,id):
        student=Students.objects.get(id=id)
        student.delete()
        return Response({"message":"Deleted sucessfully"})