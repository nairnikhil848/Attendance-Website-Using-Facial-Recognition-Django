from django.shortcuts import redirect, render, get_object_or_404
from django.http import HttpResponse, request
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
from .form import *
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.http.response import HttpResponseRedirect, StreamingHttpResponse
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
import csv
from .camera import *
# from django.shortcuts import (render_to_response)
from django.template import RequestContext
from datetime import datetime
import pytz
from .models import *
from django.views.decorators import gzip
from django.http import StreamingHttpResponse
import cv2
import threading
import numpy as np
from io import BytesIO
import base64
from cv2.cv2 import imread
import io
from PIL import Image
# from_zone = tz.gettz('UTC')
# to_zone = tz.gettz('Asia/Kolkata')

# Create your views here.


def homepage(request):
    return render(request, 'classroom/index.html')


def com_register(request):
    return render(request, 'classroom/registration.html')


def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
            if request.user.is_authenticated:
                print("here")
                if request.user.is_teacher:
                    return redirect('teacher_landing')
                else:
                    return redirect('student_landing')
            print("not authenticated")
        else:
            messages.info(request, 'Username or Password Incorrect')

    context = {}
    return render(request, 'classroom/login.html', context)


def logoutPage(request):
    logout(request)
    return redirect('login')


def home(request):
    if request.user.is_authenticated:
        if request.user.is_teacher:
            return redirect('teacher_landing')
        else:
            return redirect('student_landing')

    return render(request, 'classroom/login.html')

# ----------------teacher-view-------------------------------------


class teacher_register(CreateView):
    model = User
    form_class = TeacherSignUpForm
    template_name = "classroom/teacher/register.html"

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'teacher'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        # login(self.request, user)
        return redirect('login')


class teacher_landing(CreateView):

    template_name = 'classroom/teacher/landingPage.html'

    def get_context_data(self, *args, **kwargs):
        context = super(teacher_landing, self).get_context_data(
            *args, **kwargs)
        try:
            attendance_session = Attendance_session.objects.get(
                teacher_name_id=self.request.user.id)
        except:
            attendance_session = None
        context['attendance_session'] = attendance_session
        return context

    model = Attendance_session
    fields = ('div', 'subject')

    def form_valid(self, form):
        Attendance_session = form.save(commit=False)
        Attendance_session.teacher_name_id = self.request.user.id
        Attendance_session.save()

        print("success")
        return redirect('teacher_landing')

    def form_invalid(self, form):
        name = 'Already session in that div is active'
        messages.warning(self.request, 'Error: {0}'.format(name))

        return self.render_to_response(
            self.get_context_data(request=self.request, form=form))


def teacher_info(request):
    return render(request, 'classroom/teacher/teacher-info.html')


def attendance_listing(request):
    attendance_list = Attendance_session.objects.get(
        teacher_name_id=request.user.id).attendance_list_set.all()
    context = {'attendance_list': attendance_list, }

    return render(request, 'classroom/teacher/attendance_list.html', context)


def download_list(request):
    attendance_session = Attendance_session.objects.get(
        teacher_name_id=request.user.id)
    attendance_list = Attendance_session.objects.get(
        teacher_name_id=request.user.id).attendance_list_set.all().values_list('roll_no', 'student_name', 'admission_number', 'timestamp')
    response = HttpResponse(content_type='text/csv')
    # your filename
    response['Content-Disposition'] = 'attachment; filename="attendance.csv"'

    writer = csv.writer(response)
    writer.writerow(['Rollno', 'Name', 'Admission-Number', 'Timestamp'])

    for user in attendance_list:
        writer.writerow(user)

    attendance_session.delete()

    return response

# -------------Student-view---------------------------------------------------


class student_register(CreateView):
    model = User
    form_class = StudentSignUpForm
    # classroom/student/register.html
    template_name = "classroom/student/register.html"

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'student'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        return redirect('login')


def student_landing(request):
    try:
        attendance_session = Attendance_session.objects.get(
            div=request.user.student.div)
        marked = False
        for student in attendance_session.attendance_list_set.all():
            if student.student_name == request.user.username:
                marked = True

    except:
        marked = False
        attendance_session = None
    context = {'User': get_object_or_404(Student, pk=request.user.id),
               'attendance_session': attendance_session,
               'marked': marked,
               }
    return render(request, 'classroom/student/landingPage.html', context)


def student_info(request):
    return render(request, 'classroom/student/student-info.html')


def upload_images_home(request):
    return render(request, 'classroom/student/upload_images_home.html')


def upload_images(request):
    return render(request, 'classroom/student/upload_dataset_images.html')
    # if upload_photos(user_id):
    #     return render(request, 'classroom/student/upload_images_successfull.html')
    # else:
    #     return render(request, 'classroom/student/upload_images_failed.html')


def uploadImagesSuccessfull(request):
    return render(request, 'classroom/student/upload_images_successfull.html')


def uploadImagesunSuccessfull(request):
    return render(request, 'classroom/student/upload_images_failed.html')


def SaveImages(request):
    if request.method == 'POST':
        imageArray = request.POST['ImageArray']
        count = 1
        imageContent = imageArray.split(",")
        contents = imageContent[1::2]
        for content in contents:
            save_base64Array(request.user.id, content, count)
            count += 1
        # print("successfull")
        return HttpResponse(status=200)
    print("failed")
    return HttpResponse(status=500)


def train_images(request):
    user_id = request.user.id
    if ImageTrainer(user_id):
        return render(request, 'classroom/student/imagetrained_successfull.html')
    else:
        return render(request, 'classroom/student/imagetrained_failed.html')


def FaceImageTest(request):
    return render(request, 'classroom/student/TestImage.html')


def TestImage(request):
    Testimage = request.POST['Image']
    imageContent = Testimage.split(",")[1]

    # save image
    Id = request.user.id
    dataset_dir = "dataSet/"
    Id = str(Id)
    path = os.path.join(settings.BASE_DIR, dataset_dir, Id)
    try:
        os.mkdir(path)
    except OSError as error:
        pass
    decodeit = open(path + '/' + "51" + ".jpeg", 'wb')
    decodeit.write(base64.b64decode(imageContent))
    decodeit.close()

    # face Recognition
    if face_recognition(Id):
        print(request.user.student.roll_No)
        print(request.user.student.admission_number)
        attendance_session = Attendance_session.objects.get(
            div=request.user.student.div)
        attendance_session.attendance_list_set.create(
            student_name=str(request.user.username),
            roll_no=int(request.user.student.roll_No),
            admission_number=str(request.user.student.admission_number))
        return HttpResponse(status=200)
    else:
        return HttpResponse(status=500)


def mark_attendance(request):
    id = request.user.id
    print(request.user.username)
    print(request.user.student.admission_number)
    print(request.user.roll_no)
    print(request.user.admission_number)
    # face-recognition-------------------------------------------------------------------------------------------
    if FacialRecognition(id):
        attendance_session = Attendance_session.objects.get(
            div=request.user.student.div)
        attendance_session.attendance_list_set.create(
            student_name=str(request.user.username),
            roll_no=int(request.user.student.roll_no),
            admission_number=str(request.user.student.admission_number))
        # return redirect('attendance_successfull')
        return render(request, 'classroom/student/successfull_attendance.html')

    else:
        return render(request, 'classroom/student/failed_attendance.html')


def successfull_attendance(request):
    return render(request, 'classroom/student/successfull_attendance.html')


def unsuccessfull_attendance(request):
    return render(request, 'classroom/student/failed_attendance.html')


def attendance_successfull(request):
    return redirect('student_landing')

# def attendance_notsuccessfull(request):
#     return render(request, 'classroom/student/successfull_attendance.html')

# class student_landing(CreateView):

#     template_name = 'classroom/student/landingPage.html'

#     def get_context_data(self, *args, **kwargs):
#         context = super(teacher_landing, self).get_context_data(
#             *args, **kwargs)
#         try:
#             attendance_session = Attendance_session.objects.get(
#                 div=self.request.user.Student.div)
#         except:
#             attendance_session = None
#         context['attendance_session'] = attendance_session
#         return context

#     model = Attendance_session
#     fields = ('div', 'subject')

#     def form_valid(self, form):
#         Attendance_session = form.save(commit=False)
#         Attendance_session.teacher_name_id = self.request.user.id
#         Attendance_session.save()

#         print("success")
#         return redirect('teacher_landing')

#     def form_invalid(self, form):
#         # context = super(teacher_landing, self).get_context_data(
#         #     *args, **kwargs)
#         # messages = "already session in that div is active"
#         # # context['messages'] = messages
#         # print(messages)
#         name = 'Already session in that div is active'
#         messages.warning(self.request, 'Error: {0}'.format(name))

#         return self.render_to_response(
#             self.get_context_data(request=self.request, form=form))
#         # messages.info(request, 'Username or Password Incorrect')
#         # return super().form_invalid(form)

# def registerPage(request):
#     form = UserCreationForm()

#     if request.method == "POST":
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             form.save()

#     context = {'form': form}
#     return render(request, 'classroom/registration.html', context)


# -----------------

# def camera(request):

#     return render(request, 'classroom/student/upload_images.html')

def gen(camera):
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')


def video_feed(request):
    id = request.user.id

    if upload_photos(id):
        return HttpResponse('attendance_successfull')
    else:
        return HttpResponse('<h1>attendance  was not  found</h1>')


def handler404(request):
    return render(request, "classroom/404.html")
    # response.status_code = 404
    # return response
