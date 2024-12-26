from django.shortcuts import render
from django.views import View

# Create your views here.

class Login(View):
    def get(self,request):
        return render(request,'mainloginpage.html')
    
class AdminDash(View):
    def get(self,request):
        return render(request,'Administrator/admin.html')
    
class AppointmentAdmin(View):
    def get(self,request):
        return render(request,'Administrator/appointmentadmin.html')
    
class Doctor(View):
    def get(self,request):
        return render(request,'Administrator/doctors.html')
    
class Patient(View):
    def get(self,request):
        return render(request,'Administrator/patient.html')
    
class Service(View):
    def get(self,request):
        return render(request,'Administrator/service.html')
    

# //////////////////////////////////////////////////Doctor ///////////////////////////////////
    
class DoctorDash(View):
    def get(self,request):
        return render(request,'Doctor/dd.html')
    

class AddPost(View):
    def get(self,request):
        return render(request,'Doctor/addpost.html')
    
class DoctorAppointment(View):
    def get(self,request):
        return render(request,'Doctor/doctorappoinment.html')
    
class ManagePrescription(View):
    def get(self,request):
        return render(request,'Doctor/managepriscdr.html')
    
class Notification(View):
    def get(self,request):
        return render(request,'Doctor/notification.html')
    
#///////////////////////////////////////Pharmacist////////////////////////////////////////#    
   
class PharmacistDash(View):
    def get(self,request):
        return render(request,'Pharmacist/ph.html')
      
class AddMedicine(View):
    def get(self,request):
        return render(request,'Pharmacist/addmedicineph.html')

class UserRequest(View):
    def get(self,request):
        return render(request,'Pharmacist/userrequest.html')
      