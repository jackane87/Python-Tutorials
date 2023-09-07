def sum(n, func):
    total = 0
    for num in range(1, n+1):
        total += func(num)
    return total

def square(x): 
    return x*x

def cube(x):
    return x*x*x

print(sum(5,cube))

