from django import forms
from .models import Student, Address

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'age', 'addresses']

class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = ['city']
