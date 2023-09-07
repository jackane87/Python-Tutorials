
def last_element(list):
    '''
    >>> last_element([]) is None
    True
    
    >>> last_element([1,2,3])
    3
    '''
    if len(list) == 0:
        return None
    else:
        return list[len(list) -1]