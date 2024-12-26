from django.forms import ModelForm

from .models import *


class Notificationform(ModelForm):
    class Meta:
        model = Notification
        fields = ( 'message')

class DoctorForm(ModelForm):
    class Meta:
        model = Doctor
        fields = ('name', 'email', 'phone', 'specialization')