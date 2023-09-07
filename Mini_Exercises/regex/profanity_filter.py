import re
#This was my original solution.
def censor(input):
    censor_pattern = re.compile(r'frack[a-z]*', re.I)
    return censor_pattern.sub('CENSORED', input)

#Updated solution to account for situations where 'frack' could appear in the middle of a legitamate workd.
def censor(input):
    censor_pattern = re.compile(r'\bfrack[a-z]*\b', re.I)
    return censor_pattern.sub('CENSORED', input)

print(censor('Frack you'))