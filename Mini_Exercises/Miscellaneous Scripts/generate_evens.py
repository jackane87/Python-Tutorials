#Define a function called generate_evens
#It should return a list of even numbers between 1 and 50(not including 50)
def generate_evens():
    '''
    >>> generate_evens()
    [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48]
    '''
    return [num for num in range(1,50) if num%2 == 0]