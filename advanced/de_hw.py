def fix_func(func):
    def inner(n, d):
        if d == 0:
            return 0
        else:
            return n / d
    return inner

@fix_func
def divide(n, d):
    return n / d


print(divide(2, 0))