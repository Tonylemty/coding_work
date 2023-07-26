closure 閉包

def f():
    x = 1
    def qq():
        print('asdasdfsa')

    def inner():
        print(x)
        qq()
        #print(x)和qq()偷渡函式qq及x=1
    return inner

y = f()
y()