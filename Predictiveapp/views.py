from django.shortcuts import render,redirect
from django.views import View

from Predictiveapp.form import DoctorForm, Postform, medicinemodelform, prescriptionmodelform, servicetableform

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
    def DoctorForm(self,request):
        form=DoctorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('AdminDash')

    
class Patient(View):
    def get(self,request):
        return render(request,'Administrator/patient.html')
    
class Service(View):
    def get(self,request):
        return render(request,'Administrator/service.html')
    def servicetableform(self,request):
        form=servicetableform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('AdminDash')

    

# //////////////////////////////////////////////////Doctor ///////////////////////////////////
    
class DoctorDash(View):
    def get(self,request):
        return render(request,'Doctor/dd.html')
    

class AddPost(View):
    def get(self,request):
        return render(request,'Doctor/addpost.html')
    def post(self,request):
        form=Postform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('DoctorDash')

    
class DoctorAppointment(View):
    def get(self,request):
        return render(request,'Doctor/doctorappoinment.html')
    
class ManagePrescription(View):
    def get(self,request):
        return render(request,'Doctor/managepriscdr.html')
    def post(self,request):
        form=prescriptionmodelform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('DoctorDash')

    
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
    def medicinemodelform(self,request):
        form=medicinemodelform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('PharmacistDash')
            

class UserRequest(View):
    def get(self,request):
        return render(request,'Pharmacist/userrequest.html')
      