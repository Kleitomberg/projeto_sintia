from typing import Any

from django.contrib.auth.models import AbstractBaseUser  # type: ignore
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import UserManager as BaseUserManager
from django.db import models  # type: ignore

from users.base_model import BaseModel


class UserManager(BaseUserManager):
    def _create_user(self, password: str, **entra_fields: Any) -> Any:
        """
        Método interno para a criação de usuário padrão do sistema com senha
        criptografada

        Args:
            password (str): description
        Returns:
            Any: objeto do usuário
        """
        user = self.model(**entra_fields)
        user.set_password(password)
        user.save(using=self.db)
        return user

    def create_user(self, password: str, **extra_fields) -> Any:
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        extra_fields.setdefault('is_active', True),
        return self._create_user(password=password, **extra_fields)

    def create_superuser(self, password: str, **extra_fields) -> Any:
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(password=password, **extra_fields)


class User(AbstractBaseUser, BaseModel, PermissionsMixin):

    objects = UserManager()
    USERNAME_FIELD = 'email'

    is_staff = models.BooleanField('Staff', default=False)
    is_active = models.BooleanField('Ativo', default=True)

    solar_user_id = models.CharField('ID Solar', null=True, blank=True, max_length=50)
    email = models.EmailField('E-mail', unique=True)
    email_verified = models.BooleanField('E-mail verificado', default=False)

    first_name = models.CharField('Nome', max_length=50, blank=False, null=False)
    last_name = models.CharField('Sobrenome', max_length=50, blank=False, null=False)
    profile_picture = models.ImageField(
        'Foto de perfil',
        upload_to='profile_pictures',
        null=True,
        blank=True,
    )
    credits = models.IntegerField('Créditos', default=10)

    def credit(self, value: int) -> None:
        self.credits += value
        self.save()

    def debit(self, value: int) -> None:
        self.credits -= value
        self.save()

    def __str__(self) -> str:
        if self.first_name != '' and self.last_name != '':
            return f'{self.first_name} {self.last_name}'
        else:
            return self.email
