from django import forms
from .models import Employee

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'name of employee'
            }),
            'email': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'email of employee'
            }),
            'department': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'department of employee'
            })
        }



     
        