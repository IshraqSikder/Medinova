from django.db import models
from patients.models import Patient
from doctors.models import Doctor, AvailableTime

# Create your models here.
APPOINTMENT_STATUS = [
    ('Completed', 'Completed'),
    ('Pending', 'Pending'),
    ('Running', 'Running'),
]
APPOINTMENT_TYPES = [
    ('Offline', 'Offline'),
    ('Online', 'Online'),
]
class Appointment(models.Model):
    patient = models.ForeignKey(Patient, on_delete = models.CASCADE, blank=True, null=True)
    doctor = models.ForeignKey(Doctor, on_delete = models.CASCADE, blank=True, null=True)
    appointment_type = models.CharField(choices = APPOINTMENT_TYPES, max_length = 15)
    appointment_status = models.CharField(choices = APPOINTMENT_STATUS, max_length = 15, default = "Pending")
    symptom = models.TextField()
    time = models.ForeignKey(AvailableTime, on_delete = models.CASCADE, blank=True, null=True)
    cancel = models.BooleanField(default = False)
    
    def __str__(self):
        return f"Doctor : {self.doctor.user.first_name} , Patient : {self.patient.user.first_name}"