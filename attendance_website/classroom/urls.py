from django.urls import path
from django.conf.urls import (
    handler400, handler403, handler404, handler500
)
from . import views
import django

# handler404 = 'classroom.views.handler404'


def custom_page_not_found(request):
    return views.handler404(request)


urlpatterns = [

    path("404/", custom_page_not_found),
    path('', views.homepage, name='index'),
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutPage, name='logout'),
    path('home', views.home, name="home"),
    path('registeration/', views.com_register, name="registeration"),

    # =======student=================
    #     path('register/', views.registerPage, name='register'),
    path('student/register/', views.student_register.as_view(),
         name="student_register"),
    path('student/landingpage/', views.student_landing, name="student_landing"),
    path('student/student-info/', views.student_info, name="student_info"),
    path('student/saveImage/', views.SaveImages, name='SaveImages'),
    path('student/mark-attendance/', views.mark_attendance, name="mark_attendance"),
    #path('student/TestingImage', views.TestImage, name='TestImage'),
    path('student/UploadPhotos/successfull',
         views.uploadImagesSuccessfull, name='uploadImagesSuccessfull'),
    path('student/UploadPhotos/unsuccessfull',
         views.uploadImagesunSuccessfull, name='uploadImagesunSuccessfull'),
    path('student/mark-attendance/successfull',
         views.attendance_successfull, name="attendance_successfull"),
    path('student/TestingImage/', views.FaceImageTest, name="FaceImageTest"),
    path('student/Test-Image/', views.TestImage, name="TestImage"),
    path('student/sucessfull_attendance',
         views.successfull_attendance, name="successfull_attendance"),
    path('student/unsucessfull_attendance',
         views.unsuccessfull_attendance, name="unsuccessfull_attendance"),
    path('video_feed', views.video_feed, name='video_feed'),
    path('student/upload_images/', views.upload_images_home,
         name="upload_images_home"),
    path('student/upload_images/uploading...',
         views.upload_images, name="upload_images"),
    path('student/upload_images/train',
         views.train_images, name="train_images"),


    # ======teacher===============
    path('teacher/register/', views.teacher_register.as_view(),
         name="teacher_register"),
    path('teacher/landingpage/', views.teacher_landing.as_view(),
         name="teacher_landing"),
    path('teacher/teacher-info/', views.teacher_info, name="teacher_info"),
    path('teacher/attendance-list/',
         views.attendance_listing, name="attendance_list"),
    path('teacher/download_list/',
         views.download_list, name="download_list"),
]
