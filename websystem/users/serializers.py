import re

import django.contrib.auth.password_validation as validators
from rest_framework import serializers

from websystem.choices import ROLE_CHOICE

from .models import User


class UserDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "first_name", "last_name", "username", "email", "role", "photo")


class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "username", "email", "role")


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        max_length=65, min_length=8, write_only=True, required=True
    )
    email = serializers.EmailField(max_length=255, min_length=4, required=True)
    first_name = serializers.CharField(max_length=255, min_length=2, required=True)
    last_name = serializers.CharField(max_length=255, min_length=2, required=True)

    class Meta:
        model = User
        fields = ["username", "first_name", "last_name", "email", "password", "role"]

    def validate(self, attrs):
        email = attrs.get("email", "")
        username = attrs.get("username", "")
        validators.validate_password(attrs.get("password"))
        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError({"email": ("Email is already in use")})

        if User.objects.filter(username=username).exists():
            raise serializers.ValidationError(
                {"username": ("Username is already in use")}
            )
        return super().validate(attrs)

    def validate_password(self, password):
        if not re.findall(r"\d", password):
            raise serializers.ValidationError(
                "The password must contain at least 1 digit, 0-9."
            )
        if not re.findall("[A-Z]", password):
            raise serializers.ValidationError(
                "The password must contain at least 1 uppercase letter, A-Z."
            )
        if not re.findall("[a-z]", password):
            raise serializers.ValidationError(
                "The password must contain at least 1 lowercase letter, a-z."
            )
        if not [c for c in password if not c.isalnum()]:
            raise serializers.ValidationError(
                "The password must contain at least 1 symbol"
            )
        return password

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)


class LoginSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        max_length=128, min_length=6, write_only=True, required=True
    )
    account = serializers.CharField(max_length=128, write_only=True, required=True)

    class Meta:
        model = User
        fields = ("account", "password", "access_token", "refresh_token")
        read_only_fields = ["access_token", "refresh_token"]


class LoginResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            "username",
            "email",
            "role",
            "password",
            "access_token",
            "refresh_token",
        )
        read_only_fields = ["access_token", "refresh_token"]
