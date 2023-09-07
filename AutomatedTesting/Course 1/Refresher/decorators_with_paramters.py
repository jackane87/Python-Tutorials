import functools

user = {'username': 'jose', 'access_level': 'admin'}

def make_secure(access_level):
    def decorator(func):
    #using the wraps will keep the name and documentation (if any) of the function being passed in, instead of it being overwritten by secure_function
        @functools.wraps(func)
        def secure_function(*args, **kwargs):
            if user['access_level'] == access_level:
                return func(*args, **kwargs)
            else:
                return f'No {access_level} permissions for {user["username"]}.'
        return secure_function
    return decorator

@make_secure('admin')
def get_admin_password():
    return 'admin: 1234'

@make_secure('user')
def get_dashboard_password():
    return 'user: user_password'

print(get_admin_password())
print(get_dashboard_password())

user = {'username': 'jackson', 'access_level': 'guest'}

print(get_admin_password())
print(get_dashboard_password())