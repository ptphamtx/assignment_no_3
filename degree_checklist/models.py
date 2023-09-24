from django.db import models

# Create your models here.
class Faculty(models.Model):
    college_of = models.CharField(max_length=200, help_text="The College where the faculty is under")

    def __str__(self):
        return self.college_of


class Major(models.Model):
    major = models.CharField(max_length=200, help_text="Your Major of Study")
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE)

    def __str__(self):
        return self.major
    

class Student(models.Model):
    first_name = models.CharField(max_length=200, help_text="The Student's first name")
    last_name = models.CharField(max_length=200, help_text="The Student's last name")
    date_of_birth = models.DateField(verbose_name="Date of birth")
    major = models.ForeignKey(Major, on_delete=models.CASCADE) 
    enrollment = models.ManyToManyField("Course", through="Course_Enrollment")

    def __str__(self):
        return self.first_name


class Course(models.Model):
    course_number = models.CharField(max_length=10)
    course_name = models.CharField(max_length=200, help_text="Name of the course")
    credit_hours = models.IntegerField(help_text="Number of credit hours")
    faculty = models.ForeignKey(Faculty, on_delete=models.CASCADE)

    def __str__(self):
        return self.course_number


class Course_Enrollment(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    semester = models.CharField(max_length=10, help_text="Semester enrolled")
    year = models.IntegerField(help_text="Year enrolled")

    def __str__(self):
        return self.student
   
