from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
import datetime
from django.utils.timezone import now
# Create your models here.


class User(AbstractUser):
    is_student = models.BooleanField(default=False)
    is_teacher = models.BooleanField(default=False)


class Student(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, primary_key=True)
    admission_number = models.CharField(max_length=100, unique=True)
    divisions = (
        ('A', 'a'),
        ('B', 'b'),
        ('C', 'c'),
    )
    div = models.CharField(max_length=4, choices=divisions)
    email = models.EmailField(max_length=254, unique=True)
    roll_No = models.IntegerField(unique=False, primary_key=False, default=0)

    def __str__(self):
        return self.user.username


class Teacher(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, primary_key=True)
    email = models.EmailField(max_length=254, unique=True)

    def __str__(self):
        return self.user.username


class Attendance_session(models.Model):
    teacher_name = models.OneToOneField(
        Teacher, on_delete=models.CASCADE, primary_key=True)
    divisions = (
        ('A', 'a'),
        ('B', 'b'),
        ('C', 'c'),
    )
    div = models.CharField(
        max_length=4, choices=divisions, default="A", unique=True)
    subject = models.CharField(max_length=100, default="None")

    def __str__(self):
        return self.teacher_name.user.username


class Attendance_list(models.Model):
    attendance_session = models.ForeignKey(
        Attendance_session, on_delete=models.CASCADE)
    student_name = models.CharField(max_length=200)
    roll_no = models.IntegerField()
    admission_number = models.CharField(max_length=100)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.student_name
