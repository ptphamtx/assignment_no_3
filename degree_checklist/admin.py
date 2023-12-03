from django.contrib import admin
from degree_checklist.models import (Faculty, Course, Course_Enrollment, Student, Major)

# Register your models here.
admin.site.register(Faculty)
admin.site.register(Course)
admin.site.register(Course_Enrollment)
admin.site.register(Student)
admin.site.register(Major)

class PortalorAdminSite(admin.AdminSite):
    index_title = 'abc'
    title_header = 'cdf'
    site_header = 'ghi'
    logout_template = '/templates/logged_out.html'

