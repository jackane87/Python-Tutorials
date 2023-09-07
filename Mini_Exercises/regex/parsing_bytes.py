# don't forget to import re
import re
# define parse_bytes below:
def parse_bytes(string):
    binary_regex = re.compile(r'\b[10]{8}\b')
    match = binary_regex.findall(string)
    return match


print(parse_bytes('11010101 101 323'))

print(parse_bytes('my data is: 10101010 11100010'))