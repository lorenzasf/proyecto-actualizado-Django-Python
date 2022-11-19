from rest_framework import serializers
from .models import CustomUser

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('id', 'email','pasword', 'first_name', 'last_name')

    def create(self, validated_data):
        user = CustomUser.objects.create_user(
            username = validated_data['first_name'].lower() + "" + validated_data['last_name'].lower(),
            email = validated_data['email'],
            password = validated_data['password'],
            first_name = validated_data['first_name'],
            last_name = validated_data['last_name']
            )
        return user 


