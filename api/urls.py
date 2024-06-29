from django.urls import path

from api import views

from rest_framework.routers import DefaultRouter

router=DefaultRouter()

router.register("profile",views.ProfileView,basename="profile")

urlpatterns=[
    path('employee/',views.EmployeeListCreateView.as_view()),

    path('employee/<int:pk>/',views.EmployeeRetrieveUpdateDestroyView.as_view()),

    path('employee/department/',views.DepartmentView.as_view())

]+router.urls