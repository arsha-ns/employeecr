from django import forms
from empapp.models import Employee
class EmployeeForm(forms.Form):
    name=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))
    department=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))
    salary=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))
    location=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))
    address=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))
    

class EmployeeModelForm(forms.ModelForm):
    class Meta:
        model=Employee
        exclude=("id",)
        widgets={
            "name":forms.TextInput(attrs={"class":"form-control"}),
            "department":forms.TextInput(attrs={"class":"form-control"}),
            "salary":forms.TextInput(attrs={"class":"form-control"}),
            "location":forms.TextInput(attrs={"class":"form-control"}),
            "address":forms.TextInput(attrs={"class":"form-control"})
        }