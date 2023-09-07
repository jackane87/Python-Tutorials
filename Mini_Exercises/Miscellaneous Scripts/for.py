for x in range(1,10):
    print(x)

nums = range(1,10,2)


for num in range(10,20,2):
    print(num)


x = 0

for num in range(10,21):
    if num%2 != 0:
        x += num
        print(x)