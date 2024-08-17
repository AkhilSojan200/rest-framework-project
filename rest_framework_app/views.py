from django.shortcuts import render
from rest_framework import status, generics
from rest_framework.decorators import api_view
from rest_framework.response import Response

from rest_framework_app.models import Student
from rest_framework_app.serializers import UserSerializer


# Create your views here.

@api_view(['GET','POST'])
def student_list(request):

    if request.method =='GET':
        students = Student.objects.all()
        serializer=UserSerializer(students,many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)



@api_view(['GET','PUT','DELETE'])
def student_details(request,id):
    try:
        student = Student.objects.get(id=id)
    except Student.DoesNotExist:
        return Response(status=status.HTTP_404_Not_Found)

    if request.method== 'GET':
        serializer = UserSerializer(student)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = UserSerializer(student,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        student.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class student_class_view(generics.ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = UserSerializer


class student_view_details(generics.RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = UserSerializer