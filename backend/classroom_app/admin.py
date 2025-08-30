# Register your models here.

from django.contrib import admin
from .models import Classroom, Student

@admin.register(Classroom)
class ClassroomAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'teacher_name')
    search_fields = ('name', 'teacher_name')

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'age', 'classroom')
    search_fields = ('name',)
    list_filter = ('classroom',)