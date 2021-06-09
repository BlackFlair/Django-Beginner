from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Employee
from .serializers import EmployeesSerializer


# Create your views here.
class EmployeeList(APIView):
    def get(self, request):
        emp1 = Employee.objects.all()
        serializer = EmployeesSerializer(emp1, many=True)
        return Response(serializer.data)