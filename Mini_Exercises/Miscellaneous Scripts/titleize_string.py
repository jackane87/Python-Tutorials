def titleize(string):
    words = string.split()
    for word in words:
        words[words.index(word)] = word.capitalize()
    return ' '.join(words)


test = 'THis is a tEST sTRINg'

print(test.title)