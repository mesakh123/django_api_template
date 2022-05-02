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
        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError({"email": ("Email is already in use")})

        if User.objects.filter(username=username).exists():
            raise serializers.ValidationError(
                {"username": ("Username is already in use")}
            )
        return super().validate(attrs)

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)


class LoginSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        max_length=128, min_length=6, write_only=True, required=True
    )
    account = serializers.CharField(max_length=128, write_only=True, required=True)

    class Meta:
        model = User
        fields = ("account", "password", "token")
        read_only_fields = ["token"]


class LoginResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("username", "email", "role", "password", "token")
        read_only_fields = ["token"]
