from django.shortcuts import render


from rest_framework.views import APIView

from rest_framework.response import Response

from rest_framework import viewsets

from empapp.models import Employee,profile

from api.serializers import EmployeeSerializer,ProfileSerializer




# Create your views here.
class EmployeeListCreateView(APIView):

    def get(self,request,*args,**kwargs):

        qs=Employee.objects.all()

        serializer_instance=EmployeeSerializer(qs,many=True)



        return Response(data=serializer_instance.data)
    
    def post(self,request,*args,**kwargs):

        serializer_instance=EmployeeSerializer(data=request.data,many=False)

        if serializer_instance.is_valid():

            serializer_instance.save()


            return Response(data=serializer_instance.data)
        
        else:
            return Response(data=serializer_instance.errors)
    
    


class EmployeeRetrieveUpdateDestroyView(APIView):

    def get(self,request,*args,**kwargs):

        id=kwargs.get("pk")

        emp_obj=Employee.objects.get(id=id)

        serializer_instance=EmployeeSerializer(emp_obj,many=False)

        return Response(data=serializer_instance.data)
    

    def put(self,request,*args,**kwargs):

        id=kwargs.get("pk")

        emp_obj=Employee.objects.get(id=id)

        serializer_instance=EmployeeSerializer(data=request.data,instance=emp_obj)

        if serializer_instance.is_valid():

            serializer_instance.save()

            return Response(data=serializer_instance.data)
        
        else:
            return Response(data=serializer_instance.errors)
            

        

    def delete(self,request,*args,**kwargs):

        id=kwargs.get("pk")

        Employee.objects.get(id=id).delete()

        return Response(data={"message":"delete"})
    

class DepartmentView(APIView):



    def get(self,request,*args,**kwargs):

        qs=Employee.objects.all().values_list("department",flat=True).distinct()

        return Response(data=qs)
    



class ProfileView(viewsets.ViewSet):

    def list(self,request,*args,**kwargs):

        qs=profile.objects.all()

        serilaizer_instance=ProfileSerializer(qs,many=True)

        return Response(data=serilaizer_instance.data)
    

    
    def create(self,request,*args,**kwargs):

        serializer_instance=ProfileSerializer(data=request.data,many=False)

        if serializer_instance.is_valid():

            serializer_instance.save()

            return Response(data=serializer_instance.data)
        
        else:

            return Response(data=serializer_instance.errors)
        

    def retrieve(self,request,*args,**kwargs):

        id=kwargs.get("pk")

        profile_obj=profile.objects.get(id=id)

        serializer_instance=ProfileSerializer(profile_obj,many=False)

        return Response(data=serializer_instance.data)
    

    def update(self,request,*args,**kwargs):

        id=kwargs.get("pk")

        profile_obj=profile.objects.get(id=id)

        serializer_instance=ProfileSerializer(data=request.data,instance=profile_obj)

        if serializer_instance.is_valid():

            serializer_instance.save()

            return Response(data=serializer_instance.data)
        
        else:

            return Response(data=serializer_instance.errors)
        

    def destroy(self,request,*args,**kwargs):

        id=kwargs.get("pk")

        profile.objects.get(id=id).delete()

        return Response(data={"message":"deleted"})

