from django import forms
from employees.models import Employee


class EmployeerForms(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ('name', 'age', 'pis', 'function','year_contribution', )
