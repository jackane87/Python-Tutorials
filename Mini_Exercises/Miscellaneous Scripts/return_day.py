def return_day(day):
    ''' 
    >>> return_day(2)
    'Monday'
    '''
    days = {1: 'Sunday', 2: 'Monday', 3: 'Tuesday', 4: 'Wednesday', 5: 'Thursday', 6: 'Friday', 7: 'Saturday'}
    if days.get(day):
        return days.get(day)
    
  