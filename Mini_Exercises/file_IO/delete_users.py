'''delete_users
For this exercise, you'll be working with a file called users.csv . Each row of data consists of two columns: a user's first name, and a user's last name.

Implement the following function:

delete_users : Takes in a first name and a last name. Updates the users.csv file so that any user whose first and last names match the inputs are removed. 
The function should return a count of how many users were removed.'''

'''
delete_users("Grace", "Hopper") # Users deleted: 1.
delete_users("Colt", "Steele") # Users deleted: 2.
delete_users("Not", "Here") # Users deleted: 0.
'''

#This was my solution.
from csv import reader, writer
def delete_users(fname, lname):
    with open('users.csv') as file:
        users = list(reader(file))
        removed_users = 0
        for user in users:
            if user[0] == fname and user[1] == lname:
                users.pop(users.index(user))
                removed_users += 1
    with open('users.csv', 'w') as file:
        for row in users:
            file.write(f'{row[0]},{row[1]}\n')
    return f'Users deleted: {removed_users}.' 


