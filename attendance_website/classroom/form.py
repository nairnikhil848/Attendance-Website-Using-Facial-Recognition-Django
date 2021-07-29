from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from .models import User, Student, Teacher
from django import forms


class StudentSignUpForm(UserCreationForm):

    admission_number = forms.CharField(
        required=True, )
    divisions = (
        ('A', 'a'),
        ('B', 'b'),
        ('C', 'c'),
    )

    div = forms.ChoiceField(choices=divisions,)
    rollNo = forms.IntegerField(
        required=True, )
    email = forms.EmailField(required=True,)

    class Meta(UserCreationForm.Meta):
        model = User

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_student = True
        user.save()

        student = Student.objects.create(user=user)
        student.admission_number = self.cleaned_data.get('admission_number')
        student.div = self.cleaned_data.get('div')
        student.email = self.cleaned_data.get('email')
        student.roll_No = self.cleaned_data.get('rollNo')
        student.save()

        return user


class TeacherSignUpForm(UserCreationForm):

    email = forms.EmailField(required=True)

    class Meta(UserCreationForm.Meta):
        model = User

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_teacher = True
        user.save()

        teacher = Teacher.objects.create(user=user)
        teacher.email = self.cleaned_data.get('email')
        teacher.save()

        return user


# class CreateSession(forms.ModelForm):
#     subject = forms.CharField(required=True)
#     div = forms.EmailField(required=True)
#     fields = ('div', 'subject')

#     class Meta():
#         model = Teacher

#     @transaction.atomic
#     def save(self):
#         # user = super().save(commit=False)
#         # user.is_student = True
#         # user.save()

#         Attendance_session = Attendance_session.objects.create(
#             teacher_name=Teacher)
#         Attendance_session.subject = self.cleaned_data.get('subject')
#         Attendance_session.div = self.cleaned_data.get('div')
#         Attendance_session.save()

#         return Teacher
