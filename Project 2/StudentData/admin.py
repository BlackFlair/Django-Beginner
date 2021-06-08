from django.contrib import admin
from .models import StudentDetail

# Register your models here.


class studentDetailAdmin(admin.ModelAdmin):
    fields = ['rollNo', 'name', 'age', 'course', 'phone']

admin.site.register(StudentDetail, studentDetailAdmin)