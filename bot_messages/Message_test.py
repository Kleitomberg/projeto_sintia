from rest_framework.authtoken.models import Token  # type: ignore
from rest_framework.test import APIRequestFactory, APITestCase

from bot_messages.views import MessageCreateView
from users.models import User


class TestMessageView(APITestCase):
    def setUp(self) -> None:
        self.factory = APIRequestFactory()
        self.view = MessageCreateView.as_view()
        self.uri = '/api/message/create'
        self.user = User.objects.create_user(
            email='betoxedon@hotmail.com',
            password='1234567890x',
            first_name='Roberto',
            last_name='Melo',
        )
        self.token = Token.objects.create(user=self.user)

    def test_create_message(self) -> None:
        data = {'prompt': 'test', 'message_session': None}

        factory = APIRequestFactory()
        request = factory.post(self.uri, data, format='json')
        response = self.view.as_view()(request)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, {'message': 'Hello World!'})
