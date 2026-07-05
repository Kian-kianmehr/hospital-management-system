from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
from django.contrib.auth import authenticate

from .models import (
    User,
    PatientProfile,
)


class RegisterSerializer(serializers.ModelSerializer):

    confirm_password = serializers.CharField(
        write_only=True
    )

    class Meta:
        model = User

        fields = (
            "username",
            "email",
            "password",
            "confirm_password",
        )

        extra_kwargs = {
            "password": {
                "write_only": True
            }
        }

    def validate_email(self, value):

        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError(
                "This email is already in use."
            )

        return value

    def validate(self, attrs):

        if attrs["password"] != attrs["confirm_password"]:
            raise serializers.ValidationError(
                {
                    "confirm_password": "Passwords do not match."
                }
            )

        validate_password(attrs["password"])

        return attrs

    def create(self, validated_data):

        validated_data.pop("confirm_password")

        password = validated_data.pop("password")

        user = User(**validated_data)
        user.set_password(password)

        user.role = User.Role.PATIENT

        user.save()

        PatientProfile.objects.create(
            user=user
        )

        return user
    

class PatientProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = PatientProfile

        fields = (
            "date_of_birth",
            "gender",
            "phone_number",
            "address",
            "chronic_disease_description",
        )
    

class LoginSerializer(serializers.Serializer):

    username = serializers.CharField()

    password = serializers.CharField(
        write_only=True
    )

    def validate(self, attrs):

        user = authenticate(
            username=attrs["username"],
            password=attrs["password"],
        )

        if user is None:
            raise serializers.ValidationError(
                "Invalid username or password."
            )

        attrs["user"] = user

        return attrs