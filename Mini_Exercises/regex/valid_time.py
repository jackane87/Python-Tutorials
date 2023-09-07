# Don't forget to import re!
import re

# Define is_valid_time below:
def is_valid_time(string):
    time_regex = re.compile(r'^\d\d?:]d{2}$')
    match = time_regex.search(string)
    if match:
        return True
    return False


print(is_valid_time('10:45'))