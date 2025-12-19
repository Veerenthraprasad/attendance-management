from rest_framework import serializers
from .models import User
import random
import string


class UserCreateSerializer(serializers.ModelSerializer):
    generated_password = serializers.CharField(read_only=True)

    class Meta:
        model = User
        fields = (
            "id",
            "user_id",
            "name",
            "role",
            "staff_category",
            "generated_password",
        )

    def create(self, validated_data):
        password = "".join(random.choices(string.ascii_letters + string.digits, k=8))

        user = User.objects.create_user(
            user_id=validated_data["user_id"],
            password=password,
            name=validated_data["name"],
            role=validated_data["role"],
            staff_category=validated_data.get("staff_category"),
            is_staff=True if validated_data["role"] != "STAFF" else False,
        )

        validated_data["generated_password"] = password
        user.generated_password = password
        return user


class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            "id",
            "user_id",
            "name",
            "role",
            "staff_category",
            "is_active",
        )


class MeSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = (
            "user_id",
            "name",
            "role",
            "staff_category",
        )
