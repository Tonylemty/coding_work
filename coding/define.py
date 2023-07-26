def wash(dry=False, water=8):
    print('加水', water, '分滿')
    print('加洗衣精')
    print('旋轉')
    if dry:
       print('烘衣')

wash(water = 10)


def say_hi():
    print('hi')

#say_hi()

def add(x, y):
     return x + y

result = add(3, 4)
print(result)


def average(numbers):
    return sum(numbers) / len(numbers)
print(average([1, 2 ,3]))
print(average([23, 32, 6]))
