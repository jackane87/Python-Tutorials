user_age = int(input('How old are you? '))

months = user_age * 12
#seconds calculated by multiplying number of years by 365 days, by 24 hours by 60 minutes by 60 seconds.
seconds = user_age*365*24*60*60

print(f'{user_age} years is equal to {months} months. It is also equal to {seconds} seconds.')