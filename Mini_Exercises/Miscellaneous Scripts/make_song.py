'''
kombucha_song = make_song(5, "kombucha")
next(kombucha_song) # '5 bottles of kombucha on the wall.'
next(kombucha_song) # '4 bottles of kombucha on the wall.'
next(kombucha_song) # '3 bottles of kombucha on the wall.'
next(kombucha_song) # '2 bottles of kombucha on the wall.'
next(kombucha_song) # 'Only 1 bottle of kombucha left!'
next(kombucha_song) # 'No more kombucha!'
next(kombucha_song) # StopIteration

default_song = make_song()
next(default_song) # '99 bottles of soda on the wall.'
'''
#This was my original solution I came up with on my own.
'''def make_song(count=99, beverage='soda'):
    count = count
    while count > -1:
        if count == 0:
            yield f'No more {beverage}!'
            count -= 1
        elif count == 1:
            yield f'Only 1 bottle of {beverage} left!'
            count -= 1
        else:
            yield f'{count} bottles of {beverage} on the wall.'
            count -= 1'''

#This was the posted solution exercise.
def make_song(verses=99, beverage="soda"):
    for num in range(verses, -1, -1):
        if num > 1:
            yield f"{num} bottles of {beverage} on the wall."
        elif num == 1:
            yield f"Only 1 bottle of {beverage} left!"
        else:
            yield f"No more {beverage}!"

soda_song = make_song(5)

for verse in soda_song:
    print(verse)