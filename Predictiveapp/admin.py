from django.contrib import admin

from .models import *

# Register your models here.

admin.site.register(Loginmodel)
admin.site.register(Doctor)
admin.site.register(Notification)