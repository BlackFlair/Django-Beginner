from django.shortcuts import render
from .models import StudentDetail

# Create your views here.
def index(request):
    studentList = StudentDetail.objects.all()
    return render(request, 'index.html', {'studentList':studentList})