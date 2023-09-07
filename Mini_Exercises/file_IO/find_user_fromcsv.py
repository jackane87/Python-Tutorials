'''find_user("Colt", "Steele") # 1
find_user("Alan", "Turing") # 3
find_user("Not", "Here") # 'Not Here not found.'
'''
from csv import DictReader
def find_user(fname, lname):
    with open('users.csv') as file:
        users = list(DictReader(file))
        for user in users:
            if user['First Name'] == fname and user['Last Name'] == lname:
                return users.index(user)
        return f'{fname} {lname} not found.'
    
print(find_user('Jim', 'Jones'))
print(find_user('Alan', 'Turing'))


