from django.shortcuts import render
from rest_framework import viewsets
from . import models, serializers

# Create your views here.
class ContactusViewset(viewsets.ModelViewSet):
    queryset = models.ContactUs.objects.all()
    serializer_class = serializers.ContactUsSerializer