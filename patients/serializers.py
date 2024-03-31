from rest_framework import serializers
from .models import Patient
from django.contrib.auth.models import User

class PatientSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(many=False)
    class Meta:
        model = Patient
        fields = '__all__'

class RegistrationSerializer(serializers.ModelSerializer):
    confirm_password = serializers.CharField(required=True)
    image = serializers.ImageField(required=False)
    profession = serializers.CharField(required=False)
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password', 'confirm_password', 'image', 'profession']

    def save(self):
        username = self.validated_data['username']
        first_name = self.validated_data['first_name']
        last_name = self.validated_data['last_name']
        email = self.validated_data['email']
        password = self.validated_data['password']
        password2 = self.validated_data['confirm_password']
        image = self.validated_data.get('image', None)
        profession  = self.validated_data['profession']

        if password != password2:
            raise serializers.ValidationError({'error': "Passwords do not match"})
        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError({'error': "Email already exists"})

        user = User(username=username, email=email, first_name=first_name, last_name=last_name)
        user.set_password(password)
        user.is_active = False
        user.save()
        
        Patient.objects.create(user=user, image=image, profession=profession)
            
        return user

class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField(required = True)
    password = serializers.CharField(required = True)