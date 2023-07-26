def wash(dry=False, water=8): #define(def)定義一個function 
    print('加水', water, '分滿')
    print('加洗衣精')
    print('旋轉')
    if dry: #dry叫做參數
        print('烘衣')

wash(water=10) #使用function

def add(x, y): #x, y的預設值為0
    return x + y 

result = add(3, 4)
print(result)

def average(numbers):
    return sum(numbers) / len(numbers)
print(average([1, 2, 3]))
print(average([23, 32, 6]))
print(average([180, 34, 92]))