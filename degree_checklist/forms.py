from .models import Faculty, Course, Major, Student, Course_Enrollment
from django import forms


class RegistrationForm(forms.ModelForm):
    semester_choice = (("1", "Spring"), ("2", "Summer"), ("3", "Fall"), ("4", "Winter"))
    year = forms.IntegerField(min_value=2023, help_text= "Must be this current year or later")
    semester = forms.ChoiceField(choices = semester_choice)
    class Meta:
        model = Course_Enrollment
        fields = "__all__"


class UploadForm(forms.ModelForm):
    file_upload = forms.FileField()
    class Meta:
        model = Student
        fields = ("first_name", "last_name", "file_upload")