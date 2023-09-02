from django.contrib import admin
from .models import Student

# Register your models here.
class AdminStudent(admin.ModelAdmin):
    list_display=['name','subject','fee','department','rate']
admin.site.register(Student,AdminStudent)
