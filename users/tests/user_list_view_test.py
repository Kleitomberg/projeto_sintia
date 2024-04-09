from rest_framework.test import APIRequestFactory

from users.tests.user_test_base import UserBaseTest
from users.views import UserListView


class UserListViewTest(UserBaseTest):
    def setUp(self) -> None:
        self.factory = APIRequestFactory()
        self.view = UserListView.as_view()
        self.url = '/users/'
        super().setUp()

    def test_if_view_raises_permission_denied_error(self):
        request = self.factory.get(self.url)
        response = self.view(request)
        self.assertEqual(
            response.status_code,
            403,
            'Expected Response Code 403, received {0} instead.'.format(
                response.status_code,
            ),
        )

    def test_if_authenticated_user_gets_200(self):
        request = self.factory.get(
            self.url,
            headers={'Authorization': f'Token {self.token}'},
        )
        response = self.view(request)
        self.assertEqual(response.status_code, 200)

    def test_if_authenticated_user_gets_his_info(self):
        request = self.factory.get(
            self.url,
            headers={'Authorization': f'Token {self.token}'},
        )
        response = self.view(request)
        self.assertEqual(response.data.serializer.instance[0], self.user)
