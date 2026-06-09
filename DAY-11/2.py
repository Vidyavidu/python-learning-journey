def sum_first_n(n):
    if n == 0:
        return 0
    return n + sum_first_n(n - 1)


print(sum_first_n(5))
