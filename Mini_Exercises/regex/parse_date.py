#define parse_date below
import re
def parse_date(string):
    date_regex = re.compile(r'^(?P<d>[0123]\d{1})(/|,|\.)(?P<m>[01]\d{1})(/|,|\.)(?P<y>\d{4})$')
    match = date_regex.search(string)
    if match:
        return {'d': match.group('d'), 'm': match.group('m'), 'y': match.group('y')}
    return None

print(parse_date('31/12/1987'))

print(parse_date('113/25/2001'))

print(parse_date('31,12,1987'))

print(parse_date('02.11.1999'))