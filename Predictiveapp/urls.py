
from django.contrib import admin
from django.urls import include, path

from .views import *

urlpatterns = [
    path('', Login.as_view(),name='login'),
    path('admindash', AdminDash.as_view(),name='admindash'),
    path('appointmentadmin',AppointmentAdmin.as_view(),name='appointmentadmin'),
    path('doctor',Doctor.as_view(),name='doctor'),
    path('patient',Patient.as_view(),name='patient'),    
    path('service',Service.as_view(),name='service'), 
# //////////////////////////////////////////////////Doctor ///////////////////////////////////
   
    path('doctordash',DoctorDash.as_view(),name='doctordash'),    
    path('addpost',AddPost.as_view(),name='addpost'),    
    path('adddoctor',Adddoctor.as_view(),name='adddoctor'),
    path('doctorappointment',DoctorAppointment.as_view(),name='doctorappointment'),   
    path('manageprescription',ManagePrescription.as_view(),name='manageprescription'),  
    path('notification',Notification.as_view(),name='notification'),

#///////////////////////////////////////Pharmacist////////////////////////////////////////#    
path('pharmacistdash',PharmacistDash.as_view(),name='pharmacistdash'),
path('addmedicine',AddMedicine.as_view(),name='addmedicine'),
path('userrequest',UserRequest.as_view(),name='userrequest'),

]
