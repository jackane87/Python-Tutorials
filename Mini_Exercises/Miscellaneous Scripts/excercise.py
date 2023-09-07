def sum_all_nums(*args):
    total = 0
    for num in args:
        if num % 2 == 0:
            total += num
        else:
            pass
    return total


print(sum_all_nums(1,3,7))
