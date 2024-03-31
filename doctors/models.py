from django.db import models
from django.contrib.auth.models import User
from patients.models import Patient
from .constants import STAR_CHOICES

# Create your models here.
class Specialization(models.Model):
    name = models.CharField(max_length = 30)
    slug = models.SlugField(max_length = 40)
    def __str__(self):
        return self.name
        
class AvailableTime(models.Model):
    name = models.CharField(max_length = 100)
    
    def __str__(self):
        return self.name

class Doctor(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    description = models.TextField()
    image = models.ImageField(upload_to="doctors/images/")
    specialization =  models.ManyToManyField(Specialization)
    available_time = models.ManyToManyField(AvailableTime)
    fee = models.IntegerField()
    meet_link = models.CharField(max_length = 100)
    
    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"

class Review(models.Model):
    reviewer = models.ForeignKey(Patient, on_delete = models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete = models.CASCADE)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add = True)
    rating = models.CharField(choices = STAR_CHOICES, max_length = 10)
    
    def __str__(self):
        return f"Patient : {self.reviewer.user.first_name} ; Doctor : {self.doctor.user.first_name}"