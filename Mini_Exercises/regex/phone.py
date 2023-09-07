import re

#Returns the first phone number found in string.
def extract_phone(input):
    phone_regex = re.compile(r'\b\d{3} \d{3}-\d{4}\b')
    try:
        match = phone_regex.search(input)
        return match.group()
    except AttributeError as err:
        print(err)

#Returns a list of all phone numbers found in string.
def extract_all_phones(input):
    phone_regex = re.compile(r'\b\d{3} \d{3}-\d{4}\b')
    try:
        return phone_regex.findall(input)
    except AttributeError as err:
        print(err)

#Returns true or false if input is only a valid phone number. Using the search method, we need to include the ^ for starts with and $ for ends with.
'''def is_valid_phone(input):
    phone_regex = re.compile(r'^\d{3} \d{3}-\d{4}$')
    match = phone_regex.search(input)
    if match:
        return True
    return False'''

#Returns true or false if input is only a valid phone number. Using the fullmatch method, we DONT need to include the ^ for starts with and $ for ends with.
def is_valid_phone(input):
    phone_regex = re.compile(r'\d{3} \d{3}-\d{4}')
    match = phone_regex.fullmatch(input)
    if match:
        return True
    return False






print(extract_phone('my number is 987 654-3210'))

print(extract_phone('my number is 223 654-3987012'))

print(extract_all_phones('my number is 223 654-3987 and 555 555-5555'))