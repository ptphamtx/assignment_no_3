from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Faculty, Course, Student, Major, Course_Enrollment
from .forms import RegistrationForm
from django.contrib import messages

# Create your views here.
def registration_edit(request, pk=None):
    if pk is not None:
        register = get_object_or_404(Course_Enrollment, pk=pk)
    else:
        register = None
    if request.method == "POST":
        form = RegistrationForm(request.POST, instance = register)
        if form.is_valid():
            updated_register = form.save()
            if register is None:
                messages.success(request, '"{}" was successfully registered.'.format(updated_register))
            else:
                messages.success(request, '"{}" was successfully updated.'.format(updated_register))
            return redirect("register_edit", updated_register.pk)
    else:
        form = RegistrationForm(instance = register)
    return render(request, "registration_form.html", {"method": request.method, "form": form})


def test_view(request):
    return render(request, 'base.html')


def welcome_view(request):
    return render(request, 'home.html')


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


def course_enrollment_list(request):
    course_enrollments = Course_Enrollment.objects.all()
    ce_list = []
    for item in course_enrollments:
        ce_list.append({'all': item})
    course_enrollment = {
        'ce_list': ce_list
    }       
    return render(request, 'course_enrollment.html', course_enrollment)



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
