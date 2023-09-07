import re
url_regex = re.compile(r'(https?)://(www\.[A-Za-z-]{2,256}\.[a-z]{2,6})([-a-zA-Z0-9@:%_\+.~#?&//=]*)')

match = url_regex.search('https://www.youtube.com/videos/cats')

print(match.group())

print(match.groups())