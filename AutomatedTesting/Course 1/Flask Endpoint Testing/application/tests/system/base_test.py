from unittest import TestCase
from app import app

#setting up a BaseTest class that can be used across multiple test files.
class BaseTest(TestCase):
    def setUp(self):
        #this will always run the flask app in testing mode.
        app.testing = True
        self.app = app.test_client