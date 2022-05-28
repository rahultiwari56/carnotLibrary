import email
from django.http import HttpResponse, HttpResponseForbidden
from django.shortcuts import render
from django.forms.models import model_to_dict
from django.http import JsonResponse, HttpResponse
from library.models import Student, School, Book
from django.views.decorators.csrf import csrf_exempt

def index(request):
    student = Student.objects.all().count()
    book = Book.objects.all().count()
    school = School.objects.all().count()
    print(student)
    return render(request, 'index.html', {'total_student': student, 'total_school': school, 'total_book': book})

def find_student(request):
    return render(request, 'search_student.html')

@csrf_exempt
def add_student(request):
    if request.method == 'POST':
        # student data
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        student_email = request.POST.get('student_email')
        gender = request.POST.get('gender')
        # school data
        school_region_id = request.POST.get('school_region_id')
        school_name = request.POST.get('school_name')
        school_email = request.POST.get('school_email')
        school_principal = request.POST.get('school_principal')
        school_phone = request.POST.get('school_phone')
        school_address = request.POST.get('school_address')
        # book data
        book_title = request.POST.get('book_title')
        book_author = request.POST.get('book_author')
        book_publication_date = request.POST.get('book_publication_date')
        book_pgs_read = request.POST.get('book_pgs_read')

        students = Student.objects.filter(email=student_email)

        if len(students)!=0:
            return render(request, 'add_student.html', {"Message":"Student Already exist"})

        school = School.objects.filter(school=school_name)
        # print(school)
        if len(school)!=0:
            # get school id if it already exists
            school = model_to_dict(school[0])['id']
        else:
            if school_region_id == '':
                school_region_id = None

            # fill school data if it doesnt exists
            school_data = School(region_id=school_region_id, school=school_name, email=school_email, principal=school_principal, phone=school_phone, address=school_address)
            school_data.save()

            # get school id after saving
            school = School.objects.filter(school=school_name)
            school = model_to_dict(school[0])['id']

        # print(f'school id is {school}')

        book = Book.objects.filter(Title=book_title)
        print(book)
        if len(book)!=0:
            # get school id if it already exists
            book = model_to_dict(book[0])['id']
        else:
            if book_pgs_read=='':
                book_pgs_read = None
                if book_publication_date=='':
                    book_publication_date = None
                # fill book data if it doesnt exists
                book_data = Book(Title=book_title, Author_Name=book_author, Date_Of_Publication=book_publication_date)
                book_data.save()
            else:
                book_pgs_read = None
                # fill book data if it doesnt exists
                book_data = Book(Title=book_title, Author_Name=book_author, Date_Of_Publication=book_publication_date, Number_Of_Pages=book_pgs_read)
                book_data.save()

            # get book id after saving
            book = Book.objects.filter(Title=book_title)
            book = model_to_dict(book[0])['id']

        # print(f'book id is {book}')

        student_data = Student(first_name=first_name, last_name=last_name, email=student_email, gender=gender,
        school=School.objects.get(id=school),
        book=Book.objects.get(id=book))
        student_data.save()
        
        return render(request, 'add_student.html', {'Message': 'Addedd Successfully'})

    return render(request, 'add_student.html', {'Message': ''})


# get studen data by 'id' or 'name'
@csrf_exempt
def get_data(request):
    if request.method == "GET":
        student_id = request.GET.get("id")
        student_name = request.GET.get("name").title()

        student_data = []
        if student_id:
            students = Student.objects.filter(id=student_id).prefetch_related('school','book')
        elif student_name:
            students = Student.objects.filter(first_name=student_name).prefetch_related('school','book')
        else: 
            return HttpResponseForbidden()

        for student in students:
            try:
                school = model_to_dict(student.school)
                school_name = school['school']
                school_phone = school['phone']
            except:
                school_name = ''
                school_phone = ''

            try:
                book = model_to_dict(student.book)
                book_title = book['Title']
                total_read_pgs = book['Number_Of_Pages']
            except:
                book_title = ''
                total_read_pgs = ''

            student = model_to_dict(student)

            student_data.append({
                "student_id": f"{student['id']}",
                "student_full_name": f"{student['first_name']} {student['last_name']}",
                "student_email": student['email'],
                "gender": student['gender'],
                "school_name": school_name,
                "school_phone": school_phone,
                "book_name": book_title,
                "total_pg_read": total_read_pgs,
            })
            
        return JsonResponse({"student_data": student_data})
    else:
        return JsonResponse({"Message":"Invalid request"})
        


# get student details by id
@csrf_exempt
def get_student(request, id):
    if request.method == "GET":
        # student = Student.objects.filter(id=id).prefetch_related('school','book')
        try:
            student = Student.objects.get(id=id)
        except:
            return JsonResponse({"Message":"Id doesnt exists"})
        student_data = []
        try:
            school = model_to_dict(student.school)
            school_name = school['school']
            school_phone = school['phone']
        except:
            school_name = ''
            school_phone = ''

        try:
            book = model_to_dict(student.book)
            book_title = book['Title']
            total_read_pgs = book['Number_Of_Pages']
        except:
            book_title = ''
            total_read_pgs = ''

        student = model_to_dict(student)

        student_data.append({
            "student_id": f"{student['id']}",
            "student_full_name": f"{student['first_name']} {student['last_name']}",
            "student_email": student['email'],
            "gender": student['gender'],
            "school_name": school_name,
            "school_phone": school_phone,
            "book_name": book_title,
            "total_pg_read": total_read_pgs,
        })

        return JsonResponse({"student_data": student_data})
    else:
        return JsonResponse({"Message":"Invalid request"})