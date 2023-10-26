from tests.base_test import BaseTest
from models.user import UserModel


class UserTest(BaseTest):
    """Class representing integration tests for the User model"""
    def test_crud(self):
        """Method tests the save_to_db instance method and the find_by_username and find_by_id class methods"""
        with self.app_context():
            user = UserModel('Username1', 'Password1')
            #This check confirms that nothing has been added to the database.
            self.assertIsNone(UserModel.find_by_id(1))
            #This check confirms that Username1 specifically hasn't been added to the database.
            self.assertIsNone(UserModel.find_by_username('Username1'))

            user.save_to_db()

            #This check confirms that an single item has been added to the database and was given ID 1.
            self.assertIsNotNone(UserModel.find_by_id(1))
            #This check confirms that Username1 specifically has been added to the database.
            self.assertIsNotNone(UserModel.find_by_username('Username1'))

            