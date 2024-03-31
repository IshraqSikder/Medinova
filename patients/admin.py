from django.contrib import admin
from . import models

# Register your models here.
class PatientAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'email', 'image', 'profession']
    
    def first_name(self,obj):
        return obj.user.first_name
    
    def last_name(self,obj):
        return obj.user.last_name
    
    def email(self,obj):
        return obj.user.email
      
admin.site.register(models.Patient, PatientAdmin)