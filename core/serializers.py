from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password
from django.core import exceptions as django_exceptions
from rest_framework import serializers
from djoser.serializers import UserCreateSerializer as BaseUserCreateSerializer
from djoser.serializers import UserSerializer as BaseUserSerializer


User = get_user_model()


class UserCreateSerializer(BaseUserCreateSerializer):
    name = serializers.CharField(max_length=255, source="first_name")

    class Meta(BaseUserCreateSerializer.Meta):
        fields = ["id", "username", "name", "password"]

    def validate(self, attrs):
        attrs["email"] = attrs["username"]
        user = User(**attrs)
        password = attrs.get("password")

        try:
            validate_password(password, user)
        except django_exceptions.ValidationError as e:
            serializer_error = serializers.as_serializer_error(e)
            raise serializers.ValidationError(
                {"password": serializer_error["non_field_errors"]}
            )

        return attrs


class UserSerializer(BaseUserSerializer):
    class Meta(BaseUserSerializer.Meta):
        fields = ["id", "username", "first_name", "last_name"]
