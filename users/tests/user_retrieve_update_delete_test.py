from rest_framework.test import APIRequestFactory

from users.tests.user_test_base import UserBaseTest
from users.views import UserRetrieveUpdateDestroy


class UserTestCase(UserBaseTest):
    def setUp(self) -> None:
        super().setUp()
        self.factory = APIRequestFactory()
        self.view = UserRetrieveUpdateDestroy.as_view()
        self.uri = '/users/'
        self.another_user = self.createUser()

    def test_if_view_retrieves_a_list_of_users(self):
        request = self.factory.get(
            self.uri,
            headers={'Authorization': f'Token {self.token}'},
        )
        response = self.view(request, pk=self.user.pk)
        self.assertEqual(
            response.status_code,
            200,
            'Expected Response Code 200, received {0} instead.'.format(
                response.status_code,
            ),
        )

    def test_if_view_updates_user(self):
        request = self.factory.patch(
            self.uri,
            headers={'Authorization': f'Token {self.token}'},
            data={'first_name': 'edited_name'},
        )
        response = self.view(request, pk=self.user.pk)
        self.assertEqual(
            response.status_code,
            200,
            'Expected Response Code 200, received {0} instead.'.format(
                response.status_code,
            ),
        )
        self.assertEqual(response.data['first_name'], 'edited_name')

    def test_if_raises_error_when_another_user_tries_to_update_user(self):
        request = self.factory.patch(
            self.uri,
            headers={'Authorization': f'Token {self.token}'},
            data={'first_name': 'edited_name'},
        )
        response = self.view(request, pk=self.another_user.pk)
        self.assertEqual(
            response.status_code,
            403,
            'Expected Response Code 200, received {0} instead.'.format(
                response.status_code,
            ),
        )
        self.assertEqual(
            response.data['detail'],
            'Você não tem permissão para editar este usuário',
        )

    def test_if_view_deletes_user(self):
        request = self.factory.delete(
            self.uri,
            headers={'Authorization': f'Token {self.token}'},
        )
        response = self.view(request, pk=self.user.pk)
        self.assertEqual(
            response.status_code,
            204,
            'Expected Response Code 204, received {0} instead.'.format(
                response.status_code,
            ),
        )

    def test_if_raises_error_when_another_user_tries_to_delete_user(self):
        request = self.factory.delete(
            self.uri,
            headers={'Authorization': f'Token {self.token}'},
        )
        response = self.view(request, pk=self.another_user.pk)
        self.assertEqual(
            response.status_code,
            403,
            'Expected Response Code 403, received {0} instead.'.format(
                response.status_code,
            ),
        )
        self.assertEqual(
            response.data['detail'],
            'Você não tem permissão para excluir este usuário',
        )
