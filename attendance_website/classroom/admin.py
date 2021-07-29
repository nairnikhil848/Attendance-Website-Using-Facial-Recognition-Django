from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Teacher)
admin.site.register(User)
admin.site.register(Student)
admin.site.register(Attendance_list)


class Attendance_List(admin.StackedInline):
    model = Attendance_list
    extra = 0


class Attendance_Sess(admin.ModelAdmin):
    fieldsets = [
        ('Teacher-Name', {'fields': ['teacher_name']}),
        ('Division', {'fields': ['div']}),
        ('Subject', {'fields': ['subject']}),
    ]
    inlines = [Attendance_List]


admin.site.register(Attendance_session, Attendance_Sess)
