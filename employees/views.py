from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView
from employees.forms import EmployeerForms
from addresses.forms import AddressForm
from employees.models import Employee


class EmployeeList(ListView):
    model = Employee
    template_name = 'employees/employee_list.html'
    context_object_name = 'list'


class EmployeeCreate(TemplateView):
    template_name = 'employees/employee_forms.html'

    def get_context_data(self, **kwargs):
        context = super(EmployeeCreate, self).get_context_data(**kwargs)
        context['form'] = EmployeerForms(self.request.POST or None)
        context['form_address'] = AddressForm(self.request.POST or None)
        return context

    def post(self, requzest, *args, **kwargs):
        context = self.get_context_data(**kwargs)
        form = context['form']
        form_address = context['form_address']
        if all((form.is_valid(), form_address.is_valid())):
            address = form_address.save()
            form.instance.address = address
            form.save()
        return redirect(reverse_lazy('employees:list'))