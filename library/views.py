from django.http import HttpResponse
from django.shortcuts import render, HttpResponse
from library.models import Student, School, Book

def index(request):
    return render(request, 'index.html')

def find_student(request):
    return render(request, 'search_student.html')

def add_student(request):
    return render(request, 'add_student.html')

def get_student(request, id):
    # print(id)
    # student_details = Student.objects.filter(id=id)

    student_details = Student.objects.filter(id=id).values('id', 'first_name', 'last_name', 'email', 'gender', 'school', 'book')

    # print(student_details)
    # if student_details:
    #     details = student_details[0]
    #     print(details)
  
    return HttpResponse(student_details)