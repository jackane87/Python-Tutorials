'''find_and_replace
Write a function called find_and_replace, which takes in a file name, a word to search for, and a replacement word. Replaces all instances of the word in the file with the replacement word.

(Note: we've provided you with the first chapter of Alice's Adventures in Wonderland to give you some sample text to work with. This is also the text used in the tests.)'''

'''
find_and_replace('story.txt', 'Alice', 'Colt') 
# story.txt now contains the first chapter of my new book,
# Colt's Adventures in Wonderland
'''

#This is the solution I came up with. I originally had if list_text[i] == search_word, but this missed some of the instances of Alice
#because the split() method created instances such as 'Alice,' and 'Alice;'. To fix this, I reworked the code to determine if the search_word is in
#each index of the list. This passed the exercise, but I see a potential for error. if there was some word (name in this instance), that includes the search_word
#but should NOT be modified.
def find_and_replace(fname, search_word, replacement_word):
    with open(fname) as file:
        text = file.read()
        list_text = text.split()
        i = 0
        for i in range(len(list_text)):
            if search_word in list_text[i]:
                list_text[i] = replacement_word
            else: pass
        new_text = ' '.join(list_text)
    with open(fname, 'w') as file:
        file.write(new_text)


#This is the exercise solution. I waaaay overthought this one.
def find_and_replace(file_name, old_word, new_word):
    with open(file_name, "r+") as file:
        text = file.read()
        new_text = text.replace(old_word, new_word)
        file.seek(0)
        file.write(new_text)
        #This truncate is needed since we are overwriting the existing text and the new word MAY be shorter than the old word.
        #When we write new_text to the file, if it is shorter, some of the old text will still be in the file.
        file.truncate()

