from django.shortcuts import render,redirect

from django.views.generic import View

from empapp.models import Employee
from empapp.forms import EmployeeForm,EmployeeModelForm

# Create your views here.
class  EmployeeListView(View):

    def get(self,request,*args,**kwargs):

        qs=Employee.objects.all()

        return render(request,"emplist.html",{"data":qs})
    

class EmployeeCreateView(View):
    def get(self,request,*args,**kwargs):
        form_instance=EmployeeModelForm()
        return render(request,"emp_create.html",{"form":form_instance})
    

    def post(self,request,*args,**kwargs):
        form_instance=EmployeeModelForm(request.POST)
        if form_instance.is_valid():

            # data=form_instance.cleaned_data

            # Employee.objects.create(**data)
            form_instance.save()


            return redirect("emp-list")
        else:
            return render(request,"emp_create.html",{"form":form_instance})
        


class EmployeeDetailView(View):
    def get(self,request,*args,**kwargs):

   

    
        id=kwargs.get("pk")
        qs=Employee.objects.get(id=id)
        return render(request,"emp_detail.html",{"data":qs})
    

class EmployeeDeleteView(View):
    def get(self,request,*args,**kwargs):

        id=kwargs.get("pk")
        Employee.objects.get(id=id).delete()

        return redirect("emp-list")
    

class EmployeeUpdateView(View):
    def get(self,request,*args,**kwargs):

        id=kwargs.get("pk")
        Employee_project=Employee.objects.get(id=id)

        # dictionary={
        #     "name":Employee_project.name,
        #     "department":Employee_project.department,
        #     "salary":Employee_project.salary,
        #     "location":Employee_project.location,
        #     "address":Employee_project.address
        # }
        form_instance=EmployeeModelForm(instance=Employee_project)

        return render(request,"emp_edit.html",{"form":form_instance})
    
    def post(self,request,*args,**kwargs):

        form_instance=EmployeeForm(request.POST)
        id=kwargs.get("pk")
        if form_instance.is_valid():
            data=form_instance.cleaned_data

            Employee.objects.filter(id=id).update(**data)
            return redirect("emp-list")
        else:
            return render(request,"emp_edit.html",{"form":form_instance})
    

