from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Faculty, Course, Student, Major, Course_Enrollment
# Create your views here.

def welcome_view(request):
    return render(request, 'base.html')

def student_list(request):
    students = Student.objects.all()
    student_list = []
    courses = Course_Enrollment.objects.all()
    courses_enrolled = []
    for item in students:
        student_list.append({'student': item})
    context = {
        'student_list': student_list
    }


    return render(request, 'summary/summary.html', context)

def major_list(request):
    majors = Major.objects.all()
    major_list = []
    for item in majors:
        major_list.append({'major': item})
    program = {
        'major_list': major_list
    }
    return render(request, 'program.html', program)

def faculty_list(request):
    faculties = Faculty.objects.all()
    faculty_list = []
    for item in faculties:
        faculty_list.append({'faculty': item})
    college = {
        'faculty_list': faculty_list
    }
    return render(request, 'college.html', college)

def course_list(request):
    courses = Course.objects.all()
    course_list = []
    for item in courses:
        course_list.append({'course': item})
    course_info = {
        'course_list': course_list
    }
    return render(request, 'course.html', course_info)