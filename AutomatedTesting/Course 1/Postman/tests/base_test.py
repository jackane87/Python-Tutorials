

from unittest import TestCase
from app import app
from db import db


class BaseTest(TestCase):
    """
BaseTest

This class should be the parent class to each non-unit test.
It allows for instantiation of the database dynamically
and makes sure that it is a new, blank database each time.
"""
    #setUpClass method runs once for the class. setUp method runs for each method under the class. 
    @classmethod
    def setUpClass(cls):
        # Make sure database exists
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'
        with app.app_context():
            #this if statement was added because was getting the following error "A 'SQLAlchemy' instance has already been registered on this Flask app. Import and use that instance instead."
            if 'sqlalchemy' not in app.extensions:
                db.init_app(app)
    def setUp(self):
        with app.app_context():
            db.create_all()
        # Get a test client
        self.app = app.test_client
        self.app_context = app.app_context

    def tearDown(self):
        # Database is blank
        with app.app_context():
            db.session.remove()
            db.drop_all()
