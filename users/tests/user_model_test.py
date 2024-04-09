from users.models import User
from users.tests.user_test_base import UserBaseTest


class UserModelTest(UserBaseTest):
    def test_user_credit_function(self) -> None:
        credits = self.user.credits
        self.user.credit(1)
        self.assertEqual(credits + 1, self.user.credits)

    def test_user_debit_function(self) -> None:
        credits = self.user.credits
        self.user.debit(1)
        self.assertEqual(credits - 1, self.user.credits)

    def test_if_str_method_returns_correct_value(self) -> None:
        name = f'{self.user.first_name} {self.user.last_name}'
        self.assertEqual(str(self.user), name)

    def test_str_method_returns_email_when_user_has_no_name(self) -> None:
        another_user = self.createUser()
        self.assertEqual(str(another_user), another_user.email)

    def test_if_superuser_is_created_with_is_superuser_false(self) -> None:
        with self.assertRaises(ValueError):
            superuser = User.objects.create_superuser(
                email='superuser@test.com',
                password='password',
                is_superuser=False,
            )
            superuser.save()

    def test_if_when_superuser_is_created_with_is_staff_false(self) -> None:
        with self.assertRaises(ValueError):
            superuser = User.objects.create_superuser(
                email='superuser@test.com',
                password='password',
                is_staff=False,
            )
            superuser.save()

    def test_if_superuser_is_created(self) -> None:
        superuser = User.objects.create_superuser(
            email='superuser@test.com',
            password='password',
        )
        superuser.save()
        self.assertTrue(superuser.is_superuser)
        self.assertTrue(superuser.is_staff)
