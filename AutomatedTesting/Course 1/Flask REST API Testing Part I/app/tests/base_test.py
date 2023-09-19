from unittest import TestCase
from app import app
from db import db

#This class is the parent class to each non-unit test. It allows for instantiation of the database dynaically and makes sure that it is a new blank database each time.
class BaseTest(TestCase):
    def setUp(self):
        #this creates a database for each test
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'
        #This is a Flask context manager that loads up all the app variables and config and simulates the app running.
        with app.app_context():
            #the app is initialized
            db.init_app(app)
            #the database is created
            db.create_all()
        #this sets up a test client of the app
        self.app = app.test_client()
        #this allows us to access the app_context in our tests which allows us to load up and access the database.
        self.app_context = app.app_context




    def tearDown(self) -> None:
        #this bit tears down the database at the end of the test.
        with app.app_context():
            db.session.remove()
            db.drop_all()