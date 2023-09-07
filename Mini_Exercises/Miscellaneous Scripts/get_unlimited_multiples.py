'''
sevens = get_unlimited_multiples(7)
[next(sevens) for i in range(15)] 
# [7, 14, 21, 28, 35, 42, 49, 56, 63, 70, 77, 84, 91, 98, 105]

ones = get_unlimited_multiples()
[next(ones) for i in range(20)]
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
'''
#This was my original solution
def get_unlimited_multiples(num=1):
    multiplier = 1
    while True:
        yield num * multiplier
        multiplier += 1

#This was the exercise's example solution
'''def get_unlimited_multiples(num=1):
    next_num = num
    while True:
        yield next_num
        next_num += num'''

twos = get_unlimited_multiples(2)

for num in range(1,10):
    print(next(twos))