from django.forms import ModelForm

from .models import *


class Notificationform(ModelForm):
    class Meta:
        model = Notification
        fields = [ 'notmessage']

class DoctorForm(ModelForm):
    class Meta:
        model = Doctor
        fields = ['name','age','gender','department', 'email', 'phoneno', 'qualification']

class Postform(ModelForm):
    class Meta:
        model = Post
        fields = ['posts','caption','date','time']

class pharmacistmodelform(ModelForm):
    class Meta:
        model = pharmacistmodel
        fields = ['name','age','shopname','certificate','phoneno']

class Requestform(ModelForm):
    class Meta:
        model = Request
        fields = ['request','status','date','time']

class appointmentmodelform(ModelForm):
    class Meta:
        model = appointmentmodel
        fields = ['name','age','time','tokenno','status']   

class patientmodelform(ModelForm):
    class Meta:
        model = patientmodel
        fields = ['name','age','address','phoneno','email'] 

class medicinemodelform(ModelForm):
    class Meta:
        model = medicinemodel
        fields = ['medicinename', 'quantity', 'company','price']
    
class prescriptionmodelform(ModelForm):
    class Meta:
        model = prescriptionmodel
        fields = ['name', 'age', 'tokenno','prescription']      

class servicetableform(ModelForm):
    class Meta:
        model = servicetable
        fields = ['nameofclinic','category']
