from rest_framework import serializers
from .models import user
from rest_framework.validators import ValidationError
from rest_framework.authtoken.models import Token

class UserSerializer(serializers.ModelSerializer):
    email=serializers.CharField(max_length=100)
    username=serializers.CharField(max_length=50)
    password=serializers.CharField(min_length=8,write_only=True)

    class Meta:
        model=user
        fields=['email','username','password']

    def validate(self, attrs):
        email_already_existed=user.objects.filter(email=attrs['email']).exists()

        if email_already_existed:
            raise ValidationError(f"Enterd Email id {attrs['email']} already in user. please create another user")
        return super().validate(attrs)
    
    def create(self,validated_data):
        password = validated_data.pop('password')
        user=super().create(validated_data)
        user.set_password(password)
        user.save()
        Token.objects.create(user=user)
        return user
    
