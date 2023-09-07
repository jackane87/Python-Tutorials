'''
number_compare(1,1) # "Numbers are equal"
number_compare(1,0) # "First is greater"
number_compare(2,4) # "Second is greater"
'''

def number_compare(num1,num2):
    '''
    >>> number_compare(1,2)
    'Second is greater'

    >>> number_compare(2,1)
    'First is greater'

    >>> number_compare(2,2)
    'Numbers are equal'
    
    '''
    if num1 > num2:
        return 'First is greater'
    elif num1 < num2:
        return 'Second is greater'
    return 'Numbers are equal'
