from flask_restful import Resource, reqparse
from models.user import UserModel

class UserRegister(Resource):
    """
    This resource allows users to register by sending a POST request with 
    their username and password."""

    #parser is definied with 2 arguments, username and password
    parser = reqparse.RequestParser()
    parser.add_argument('username', type=str, required=True, help='This field cannot be blank.')
    parser.add_argument('password', type=str, required=True, help='This field cannot be blank.')

    
    def post(self):
        """post method gets the data from the parser and then attempts to find the user by username and if it does find it, then it returns an error and code 400.
         If the user does not already exist, a user is created by passing the username and password to the usermodel. The user is then saved to the database and a 
         201 code is returned.  """
        data = UserRegister.parser.parse_args()

        if UserModel.find_by_username(data['username']):
            return {'message' : 'A user with that username already exists'}, 400
        
        user = UserModel(**data)
        user.save_to_db()

        return {'message': 'User created successfully.'}, 201
