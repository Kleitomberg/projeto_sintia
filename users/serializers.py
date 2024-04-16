from rest_framework import serializers  # type: ignore
from rest_framework.authtoken.models import Token

from users.models import User

from django.contrib.auth import authenticate
from django.utils.translation import gettext_lazy as _


class AuthTokenSerializer(serializers.Serializer):
    username = serializers.CharField(
        label=_("Username"),
        write_only=True
    )
    password = serializers.CharField(
        label=_("Password"),
        style={'input_type': 'password'},
        trim_whitespace=False,
        write_only=True
    )
    token = serializers.CharField(
        label=_("Token"),
        read_only=True
    )

    def validate(self, attrs):
        username = attrs.get('username')
        password = attrs.get('password')

        if username and password:
            user = authenticate(request=self.context.get('request'),
                                username=username, password=password)

            # The authenticate call simply returns None for is_active=False
            # users. (Assuming the default ModelBackend authentication
            # backend.)
            if not user:
                msg = _('E-mail ou senha incorretos.')
                raise serializers.ValidationError(msg, code='authorization')
        else:
            msg = _('E-mail e senha são obrigatórios.')
            raise serializers.ValidationError(msg, code='authorization')

        attrs['user'] = user
        return attrs


class UserSerializer(serializers.ModelSerializer):
    token = serializers.SerializerMethodField()

    
    def get_token(self, obj):
        token, _ = Token.objects.get_or_create(user=obj)
        return token.key
    
    class Meta:
        model = User
        fields = ('id', 'email', 'first_name', 'last_name', 'password','token', 'is_superuser','email_verified','profile_picture')
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
