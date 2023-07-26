import random 

start = int(input('請決定隨機數字開始值：'))
end = int(input('請決定隨機數字結束值：'))

r = random.randint(start, end)
count = 0
while True:
    count += 1
    num = int(input('請猜數字：'))
    if num == r:
        print('你猜中了！')
        print('這是你猜的第', count, '次')
        break
    elif num > r:
        print('比答案大')

    elif num < r:
        print('比答案小')
    print('這是你猜的第', count, '次') 