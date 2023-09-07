def double(x):
    return x * 2

sequence = [1, 3, 5, 9]

doubled = [double(x) for x in sequence]

doubled2 = map(double, sequence)

doubled3 = list(map(lambda x: x * 2, sequence))

print(doubled3)