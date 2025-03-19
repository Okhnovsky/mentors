from rest_framework import serializers
from djoser.serializers import UserCreateSerializer

from users.models import CustomUser


class UserRegistrationSerializer(UserCreateSerializer):

    class Meta(UserCreateSerializer.Meta):
        fields = ('username', 'password', 'email', 'phone_number')


class MentorSerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomUser
        fields = ("username",)


class ListUserSerialiser(serializers.ModelSerializer):

    mentor = MentorSerializer()

    class Meta:
        model = CustomUser
        fields = ("username", "mentor")


class NestedUsersSerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomUser
        fields = ("username",)


class UserSerializer(serializers.ModelSerializer):

    mentor = MentorSerializer()
    users = NestedUsersSerializer(many=True)

    class Meta:
        model = CustomUser
        fields = ("password", "mentor", "users")


class UpdateUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomUser
        fields = ("email", "phone_number", "mentor")
