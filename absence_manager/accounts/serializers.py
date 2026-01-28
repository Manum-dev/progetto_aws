# accounts/serializers.py
from django.contrib.auth.models import User
from rest_framework import serializers

class RegisterSerializer(serializers.ModelSerializer):
    # Definiamo la password come write_only per non mostrarla mai nelle risposte API
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ('username', 'password', 'email', 'first_name', 'last_name')

    def create(self, validated_data):
        # Usiamo create_user per gestire correttamente l'hashing della password
        return User.objects.create_user(**validated_data)