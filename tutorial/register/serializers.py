from rest_framework import serializers
from register.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        # Pode utilizar '__all__'
        fields = ["id", "name", "email", "created", "password"]
