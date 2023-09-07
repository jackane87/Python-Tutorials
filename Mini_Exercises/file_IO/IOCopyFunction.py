'''copy
Write a function called copy, which takes in a file name and a new file name and copies the contents of the first file to the second file. 

(Note: we've provided you with the first chapter of Alice's Adventures in Wonderland to give you some sample text to work with. This is also the text used in the tests.

copy('story.txt', 'story_copy.txt') # None
# expect the contents of story.txt and story_copy.txt to be the same'''

'''copy('story.txt', 'story_copy.txt') # None
# expect the contents of story.txt and story_copy.txt to be the same
'''

#This was my solution as well as the exercise solution
def copy(fname, new_fname):
    with open(fname) as file:
        copy = file.read()
    with open(new_fname,  'w') as new_file:
        new_file.write(copy)


#this was a shorter solution from another student
def copy(file1, file2):
    with open(file1) as f1, open(file2, "w") as f2: f2.write(f1.read())


#***********************************************************************************************************************************

'''copy_and_reverse
Write a function called copy_and_reverse, which takes in a file name and a new file name and copies the reversed contents of the first file to the second file.

(Note: we've provided you with the first chapter of Alice's Adventures in Wonderland to give you some sample text to work with. This is also the text used in the tests.)'''

'''
copy_and_reverse('story.txt', 'story_reversed.txt') # None
# expect the contents of story_reversed.txt to be the reverse of the contents of story.txt
'''
#my solution as well as the exercise solution
def copy_and_reverse(fname, new_fname):
    with open(fname) as file:
        copy = file.read()
    with open(new_fname,  'w') as new_file:
        new_file.write(copy[::-1])

#this is a shorter version using a modifidied version of the example above
def copy_and_reverse(file1, file2):
    with open(file1) as f1, open(file2, "w") as f2: f2.write(f1.read()[::-1])