from django.http import HttpResponse
from django.shortcuts import render, HttpResponse

def index(request):
    return render(request, 'index.html')

def find_student(request):
    return render(request, 'search_student.html')

def add_student(request):
    return render(request, 'add_student.html')

def get_student(request, id):
    pass