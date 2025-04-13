from rest_framework import serializers
from users.models import User, FileData

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

class FileDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = FileData
        fields = '__all__'
        read_only_fields = ['uploaded_by', 'uploaded_at']
