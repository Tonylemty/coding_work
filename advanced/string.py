#string formatting

name = 'Anthony'
interger = 10
floating = 3.14

print('hi %s' % name) # 字串
print('hi %d' % interger) # 整數
print('hi %f' % floating) #小數

print('hi {}'.format(name))

print(f'hi {name}, my number is {interger}')
print(f'hi {name:<10}') # 往左對齊
print(f'hi {name:>10}') #往右對齊