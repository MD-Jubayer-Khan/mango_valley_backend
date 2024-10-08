from dj_rest_auth.registration.serializers import RegisterSerializer
from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import CustomUser

User = get_user_model()

class CustomRegisterSerializer(RegisterSerializer):
    USER_TYPE_CHOICES = (
        ('admin', 'Admin'),
        ('normal', 'Normal'),
    )
    user_type = serializers.ChoiceField(choices=USER_TYPE_CHOICES)

    def get_cleaned_data(self):
        data = super().get_cleaned_data()
        data['user_type'] = self.validated_data.get('user_type', '')
        return data

    def save(self, request):
        user = super().save(request)
        user.user_type = self.cleaned_data.get('user_type')
        user.save()
        return user

class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('id','user_type', 'username')