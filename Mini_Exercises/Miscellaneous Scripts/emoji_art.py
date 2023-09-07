'''for num in range(10):
    print('\U0001f600' * num)

x = 1
while x < 11:
    print('\U0001f600' * x)
    x += 1'''


headcount = 11
for num in range(1,headcount):
    space = (" " * (headcount - num))
    print(space + "\U0001f600" * num)