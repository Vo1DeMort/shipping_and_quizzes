from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from django.contrib.auth import authenticate
from rest_framework import serializers
from .models import CustomUser, Package


# override so that login can be done with username and password
# default is email and password
class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        username = attrs.get("username")
        password = attrs.get("password")

        user = authenticate(username=username, password=password)

        if not user:
            raise serializers.ValidationError("Invalid credentials, please try again.")

        if not user.is_active:
            raise serializers.ValidationError("User account is disabled.")

        refresh = self.get_token(user)

        return {
            "refresh": str(refresh),
            "access": str(refresh.access_token),
            "user": {
                "id": user.id,
                "username": user.username,
                "email": user.email,
            },
        }


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = CustomUser
        fields = ["username", "email", "password"]

    def create(self, validated_data):
        user = CustomUser.objects.create_user(
            username=validated_data["username"],
            email=validated_data["email"],
            password=validated_data["password"],
        )
        return user


# id,username,email
class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ["id", "username", "email"]


# not for creating but others
class PackageSerializer(serializers.ModelSerializer):
    sender = CustomUserSerializer()
    receiver = CustomUserSerializer()
    total_cost = serializers.CharField(source="get_total_cost", read_only=True)

    class Meta:
        model = Package
        fields = [
            "id",
            "sender",
            "receiver",
            "weight",
            "status",
            "total_cost",
            "created",
            "received_time",
        ]


# for creating
class PkgSerializer(serializers.ModelSerializer):
    total_cost = serializers.CharField(source="get_total_cost", read_only=True)

    class Meta:
        model = Package
        fields = ["id", "sender", "receiver", "weight", "total_cost"]
