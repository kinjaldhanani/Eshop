from rest_framework import serializers
from user_info.models import User


class SignUpSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "id",
            "username",
            "first_name",
            "last_name",
            "email",
            "password",
            "Address",
            "city",
            "country",
            "phone_number",
            "gender",
            "profile_image",
        ]

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data["username"],
            first_name=validated_data["first_name"],
            last_name=validated_data["last_name"],
            email=validated_data["email"],
            password=validated_data["password"],
            Address=validated_data["Address"],
            city=validated_data["city"],
            country=validated_data["country"],
            phone_number=validated_data["phone_number"],
            gender=validated_data['gender'],
            profile_image=validated_data["profile_image"],
        )
        # task.send_email_task.delay()
        return user


class ChangePasswordSerializer(serializers.ModelSerializer):
    old_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)

    class Meta:
        model = User
        fields = ("old_password", "new_password")