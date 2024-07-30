from rest_framework import serializers
from .models import User
from django.contrib.auth.hashers import make_password
from django.contrib.auth.password_validation import validate_password


class AccountSerializer(serializers.ModelSerializer) :
    def validate_password(self, value):
        validate_password(value)
        return make_password(value)
    
    class Meta :
        model = User
        fields = ('username','password','nickname')