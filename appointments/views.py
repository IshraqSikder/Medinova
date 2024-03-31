from django.shortcuts import render
from rest_framework import viewsets, filters
from . import models, serializers

# Create your views here.
class SearchByDoctorId(filters.BaseFilterBackend):
    def filter_queryset(self, request, query_set, view):
        doctor_id = request.query_params.get("doctor_id")
        if doctor_id:
            return query_set.filter(doctor = doctor_id)
        return query_set
    
class SearchByPatientId(filters.BaseFilterBackend):
    def filter_queryset(self, request, query_set, view):
        patient_id = request.query_params.get("patient_id")
        if patient_id:
            return query_set.filter(patient = patient_id)
        return query_set

class AppointmentViewSet(viewsets.ModelViewSet):
    queryset = models.Appointment.objects.all()
    serializer_class =  serializers.AppointmentSerializer
    filter_backends = [SearchByDoctorId, SearchByPatientId]
    
    # def get_queryset(self):
    #     queryset = super().get_queryset()
    #     print(self.request.query_params)
    #     patient_id = self.request.query_params.get('patient_id')
    #     if patient_id:
    #         queryset = queryset.filter(patient_id=patient_id)
    #     return queryset