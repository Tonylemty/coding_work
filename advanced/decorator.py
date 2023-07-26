#decorator 裝飾器
import time

def print_func(func):
    def inner():
        print('running', func.__name__)
        func()
    return inner


def time_func(func):
    def inner():
        start = time.time()
        func()
        end = time.time()
        print('elapsed', end - start, 'seconds')
    return inner

def test():
    for i in range(1000000):
        i += 1



'''
可在test function前寫
@time_func
@print_func
'''
test = print_func(test)
test = time_func(test)
#功能疊加
test()