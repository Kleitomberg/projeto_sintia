from rest_framework.authtoken.models import Token
from rest_framework.test import APIRequestFactory, APITestCase

from users.models import User


class UserBaseTest(APITestCase):
    def setUp(self) -> None:
        self.factory = APIRequestFactory()
        self.user = User.objects.create_user(
            email='betoxedon@hotmail.com',
            password='1234567890x',
            first_name='Roberto',
            last_name='Melo',
        )
        self.token = Token.objects.create(user=self.user)

    def createUser(self):
        return User.objects.create_user(
            email='test@test.com',
            password='1234567890x',
            first_name='',
            last_name='',
        )
