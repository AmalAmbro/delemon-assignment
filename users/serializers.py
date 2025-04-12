from rest_framework import serializers
from users.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'role']

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['username', "first_name", "last_name", 'email', 'password', 'role']

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

