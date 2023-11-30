from models.user import UserModel
from tests.unit.unit_base_test import UnitBaseTest

class UserTest(UnitBaseTest):
    """"Class representing all tests for the User model"""
    def test_user_creation(self):
        """Method that tests that a user is created with the correct username and password"""
        user = UserModel("Test Username", "Password123")
        self.assertEqual(user.username, 'Test Username', 'The username of the user after creation does not equal the constructor argument.')
        self.assertEqual(user.password, 'Password123', 'The password of the user after creation does not equal the constructor argument.')