from rest_framework import serializers  # type: ignore
from rest_framework.authtoken.models import Token  # type: ignore
from rest_framework.test import APIRequestFactory, APITestCase  # type: ignore

from users.models import User
from users.serializers import loginSerializer
from users.views import LoginView


class LoginViewTestCase(APITestCase):
    def setUp(self) -> None:
        self.factory = APIRequestFactory()
        self.view = LoginView.as_view()
        self.uri = '/login/'
        self.user = User.objects.create_user(
            email='betoxedon@hotmail.com',
            password='1234567890x',
            first_name='Roberto',
            last_name='Melo',
        )
        self.token = Token.objects.create(user=self.user)

    def test_login(self) -> None:
        data = {'email': 'betoxedon@hotmail.com', 'password': '1234567890x'}
        request = self.factory.post(self.uri, data, format='json')
        response = self.view(request)
        self.assertEqual(response.status_code, 200)

    def test_successful_login_returns_user_token(self) -> None:
        data = {'email': 'betoxedon@hotmail.com', 'password': '1234567890x'}
        request = self.factory.post(self.uri, data, format='json')
        response = self.view(request)
        self.assertEqual(response.data['Token'], self.token.key)

    def test_login_if_user_not_found_or_wrong_entry(self) -> None:
        data = {'email': 'betoxedon@tmail.com', 'password': 'XXXXXXXX'}
        request = self.factory.post(self.uri, data, format='json')
        response = self.view(request)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.data, {'error': 'Credenciais inválidas'})

    def test_login_validationError_when_password_is_wrong(self) -> None:
        data = {'email': 'betoxedon@hotmail.com', 'password': '1234567890x'}
        login = loginSerializer(data=data)
        login.is_valid()
        with self.assertRaises(serializers.ValidationError):
            login.validate(data=login.data)
