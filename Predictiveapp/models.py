from django.db import models

# Create your models here.
class Loginmodel(models.Model):
    username = models.CharField(max_length=100, null=True,blank=True)
    password = models.CharField(max_length=100,null=True,blank=True)
    type =models.CharField(max_length=100, null=True,blank=True)

    #//////////doctortable//////////#
class Doctor(models.Model):
    LOGINID = models.ForeignKey(Loginmodel,on_delete=models.CASCADE,null=True,blank=True)
    name = models.CharField(max_length=100, null=True,blank=True)
    age = models.IntegerField(null=True,blank=True)
    gender = models.CharField(max_length=100, null=True,blank=True)
    department =models.CharField(max_length=100, null=True,blank=True)
    email= models.EmailField(null=True,blank=True)
    phoneno = models.BigIntegerField(null=True,blank=True)
    qualification= models.CharField(max_length=100, null=True,blank=True)

#///////////notification/////////////////////
class Notification(models.Model):
    message= models.CharField(max_length=100, null=True,blank=True)
    date = models.DateField(null=True,blank=True)
    time = models.TimeField(null=True,blank=True)

#//////////post////////////////////
class Post(models.Model):
    DOCTOR = models.ForeignKey(Doctor, on_delete=models.CASCADE, null=True, blank=True)
    posts= models.FileField(upload_to='post/', null=True,blank=True)
    caption= models.CharField(max_length=100, null=True,blank=True)
    date= models.DateField(null=True,blank=True)
    time= models.TimeField(null=True,blank=True)

    #/////////////pharmacist////////////////
class pharmacistmodel(models.Model):    
    LOGINID = models.ForeignKey(Loginmodel,on_delete=models.CASCADE,null=True,blank=True)
    name = models.CharField(max_length=100, null=True,blank=True)
    age  = models.IntegerField(null =True,blank=True)
    shopname = models.CharField(max_length=100,null = True,blank=True)
    cerfificate = models.FileField(upload_to='certificate/',null = True,blank=True)
    phoneno = models.IntegerField(null = True,blank=True)



#//////////////////request///////////////////////
class Request(models.Model):
    PHARMACIST = models.ForeignKey(pharmacistmodel, on_delete=models.CASCADE, null=True, blank=True)
    Request= models.FileField(upload_to='presc/', null=True,blank=True)
    status= models.CharField(max_length=100, null=True,blank=True)
    date= models.DateField(null=True,blank=True)
    time= models.TimeField(null=True,blank=True)
    
#//////////////appointment////////////////////
class appointmentmodel(models.Model): 
    DRID = models.ForeignKey(Doctor,on_delete=models.CASCADE,null =True,blank=True)
    name = models.CharField(max_length=100,null = True,blank=True)
    age = models.IntegerField(null = True,blank=True)
    time = models.CharField(max_length=100,null = True,blank=True)
    tokenno = models.IntegerField(null = True,blank=True)
    status = models.CharField(max_length=100,null = True,blank=True)

#////////////////patient///////////////////////
class patientmodel(models.Model):
    LOGINID = models.ForeignKey(Loginmodel,on_delete=models.CASCADE,null=True,blank=True)
    name = models.CharField(max_length=100,null = True,blank=True)
    age = models.IntegerField(null = True,blank=True)
    address = models.CharField(max_length=100,null = True,blank=True)
    phoneno = models.IntegerField(null = True,blank=True)
    date = models.DateField(auto_now_add=True,null = True,blank=True)
    email = models.CharField(max_length=100,null = True,blank=True)

    


#////////////////////prescription/////////////////
class prescriptionmodel(models.Model): 
    USERID = models.ForeignKey(patientmodel,on_delete=models.CASCADE,null =True,blank=True)
    DRID = models.ForeignKey(Doctor,on_delete=models.CASCADE,null =True,blank=True)
    name= models.CharField(max_length=100,null = True,blank=True)
    age = models.IntegerField(null = True,blank=True)
    date = models.DateField(auto_now_add=True,null = True,blank=True)
    tokenno = models.IntegerField(null = True,blank=True)
    prescription = models.CharField(max_length=100,null = True,blank=True)
    
#////////////////////medicine///////////////////////
class medicinemodel(models.Model):
    PHARMACIST=models.ForeignKey(pharmacistmodel,on_delete=models.CASCADE,null=True,blank=True)
    medicinename = models.CharField(max_length=100,null = True,blank=True)
    quantity = models.IntegerField(null = True,blank=True)
    company = models.CharField(max_length=100,null = True,blank=True)
    date = models.DateField(auto_now_add=True,null = True,blank=True)
    price = models.IntegerField(null = True,blank=True)

#////////////////
class servicetable(models.Model):
    nameofclinic= models.CharField(max_length=100,null = True,blank=True)
    category=models.CharField(max_length=100,null=True,blank=True)