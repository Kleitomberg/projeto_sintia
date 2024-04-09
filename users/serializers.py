from rest_framework import serializers  # type: ignore
from rest_framework.authtoken.models import Token  # type: ignore

from users.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'email', 'first_name', 'last_name', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        ...
        password = validated_data.pop('password')
        user = User.objects.create_user(password=password, **validated_data)
        user.save()
        Token.objects.create(user=user)
        return user

    def update(self, instance, validated_data):
        instance.email = validated_data.get('email', instance.email)
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.save()
        return super().update(instance, validated_data)


class loginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(max_length=128)

    def validate(self, data):
        try:
            user = User.objects.get(email=data['email'])
            if user.check_password(data['password']):
                return user
            else:
                raise serializers.ValidationError('Senha incorreta')
        except User.DoesNotExist:
            raise serializers.ValidationError('Credenciais inválidas')
