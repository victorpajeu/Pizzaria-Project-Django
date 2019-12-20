from django.urls import path
from employees.views import EmployeeCreate

app_name = 'employees'

urlpatterns = [
    path('create/', EmployeeCreate.as_view(), name='create')
]
