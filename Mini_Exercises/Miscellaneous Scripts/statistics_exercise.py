'''statistics
Write a function called statistics, which takes in a file name and returns a dictionary with the number of lines, words, and characters in the file.

(Note: we've provided you with the first chapter of Alice's Adventures in Wonderland to give you some sample text to work with. This is also the text used in the tests.)'''


'''
statistics('story.txt') 
# {'lines': 172, 'words': 2145, 'characters': 11227}
'''
#this was my  original solution
def statistics(fname):
    with open(fname) as file:
        lines = file.readlines()
        lines_count = len(lines)
        file.seek(0)
        file_output = file.read()
        words_count = len(file_output.split())
        character_count = len(file_output)
        return {'lines': lines_count, 'words': words_count, 'characters': character_count}

#my refactored code   
def statistics(fname):
    with open(fname) as file:
        lines_count = len(file.readlines())
        file.seek(0)
        file_output = file.read()
    return {'lines': lines_count, 'words': len(file_output.split()), 'characters': len(file_output)}

#this was the exercise solution    
def statistics(file_name):
    with open(file_name) as file:
        lines = file.readlines()
 
    return { "lines": len(lines),
            #for each line in lines, the line is being split, which creates a list of each word on the line. The length of each list is captured to give us the # of words in the line, then the length for each is summed.
             "words": sum(len(line.split(" ")) for line in lines),
             #for each line in lines, the length of the line is being determined, then the length of all lines are summed.
             "characters": sum(len(line) for line in lines) }