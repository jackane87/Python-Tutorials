#write will write to a file, overwriting any existing data. If file doesn't already exist, it will be created.
with open('loremipsum2.txt', 'w') as file:
    file.write('this is not lorem ipsum\n')

#append will append text to the end of an existing file. If a file doesn't already exist it will be created.
with open('loremipsum2.txt', 'a') as file:
    file.write('this is an append\n')
    file.write('this is another append\n')

#r+ (read and write) to a file. Writing is based on the placement of the cursor. By default it starts with the cursor at the beginning. 
# It is important to note that it will overwrite the contents in that location. It also does NOT create a file if it doesn't already exist.
with open('loremipsum2.txt', '+r') as file:
    file.write('Beginning')
    file.seek(25)
    file.write('middle')