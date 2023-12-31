"""
URL configuration for project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin, auth
from django.urls import path, include
import degree_checklist.views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', degree_checklist.views.welcome_view),
    path('summary/', degree_checklist.views.student_list),
    path('program/', degree_checklist.views.major_list),
    path('college/', degree_checklist.views.faculty_list),
    path('course/', degree_checklist.views.course_list),
    path('course_enrollment/', degree_checklist.views.course_enrollment_list),
    path('registers/<int:pk>/', degree_checklist.views.registration_edit, name='register_edit'),
    path('registers/new/', degree_checklist.views.registration_edit, name='register_create'),
    path('upload/', degree_checklist.views.upload),
    path("accounts/", degree_checklist.views.logout_page.as_view(), name='logout-page'),
    path("accounts/", include(("django.contrib.auth.urls", "auth"),namespace= "accounts")),
    path("accounts/password_reset/done/", auth.views.PasswordResetDoneView.as_view(),name="password_reset_done",),
    path("accounts/reset/done/", auth.views.PasswordResetCompleteView.as_view(), name="password_reset_complete",),
    path("accounts/profile/", degree_checklist.views.profile, name = 'profile'),
]
