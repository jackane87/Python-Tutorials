import functools

user = {'username': 'jose', 'access_level': 'admin'}


def make_secure(func):
    #using the wraps will keep the name and documentation (if any) of the function being passed in, instead of it being overwritten by secure_function
    @functools.wraps(func)
    def secure_function(*args, **kwargs):
        if user['access_level'] == 'admin':
            return func(*args, **kwargs)
        else:
            return f'No admin permissions for {user["username"]}.'
    return secure_function

@make_secure
def get_password(panel):
    if panel == 'admin':
        return '1234'
    elif panel == 'billing':
        return 'super_secure_password'



print(get_password('billing'))