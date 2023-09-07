'''
evens = get_multiples(2, 3)
next(evens) # 2
next(evens) # 4
next(evens) # 6
next(evens) # StopIteration

default_multiples = get_multiples()
list(default_multiples) # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
'''

#this was my original solution using a while loop
'''def get_multiples(num=1, count=10):
    cnt = 1
    while cnt <= count:
        yield num * cnt
        cnt += 1'''

#This is my rework using a for loop
def get_multiples(number=1, count=10):
    for cnt in range(1,count +1):
        yield cnt * number

#This was the solution presented by the exercise
'''def get_multiples(num=1, count=10):
    next_num = num
    while count > 0:
        yield next_num
        count -= 1
        next_num += num'''