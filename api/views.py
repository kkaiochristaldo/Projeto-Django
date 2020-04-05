from django.shortcuts import render, redirect
from .models import Employee
from .form import EmployeeForm

def home(request):
    data = {}
    data['employees'] = Employee.objects.all()
    return render(request, 'api/home.html', data)

def create(request):
    data = {}
    form = EmployeeForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('url_home')
    data['form'] = form
    data['title'] = "Register Employee"
    return render(request, 'api/form.html', data)

def update(request, pk):
    data = {}
    employee = Employee.objects.get(pk=pk)
    form = EmployeeForm(request.POST or None, instance=employee)

    if form.is_valid():
        form.save()
        return redirect('url_home')
    data['title'] = "Edit Employee"
    data['form'] = form
    return render(request, 'api/form.html', data)    

def delete(request, pk):
    employee = Employee.objects.get(pk=pk)
    employee.delete()
    return redirect('url_home')
