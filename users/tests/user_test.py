from rest_framework.authtoken.models import Token  # type: ignore
from rest_framework.test import APIRequestFactory, APITestCase  # type: ignore

from users.models import User
from users.views import LoginView, UserCreate


class RegisterUserTestCase(APITestCase):
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

    def test_create_user_view(self) -> None:
        data = {
            'email': 'test@test.com',
            'password': '8x5j6vh3',
            'first_name': 'user',
            'last_name': 'test',
        }
        request = self.factory.post('/api/register/', data, format='json')
        response = UserCreate.as_view()(request)
        self.assertEqual(response.status_code, 201)
