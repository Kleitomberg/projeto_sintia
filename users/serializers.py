from rest_framework import serializers  # type: ignore

from users.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'email', 'first_name', 'last_name', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data: dict) -> User:
        ...
        password = validated_data.pop('password')
        user = User.objects.create_user(password=password, **validated_data)
        user.save()
        return user

    def update(self, instance: User, validated_data: dict) -> User:
        instance.email = validated_data.get('email', instance.email)
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.save()
        return super().update(instance, validated_data)
