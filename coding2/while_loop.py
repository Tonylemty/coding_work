num = 3
password = 'An930903'
while True:
    ans = input('請輸入密碼：')
    if ans == password:
        print('登入成功')
        break 
    else:
        num -= 1
        if num == 0:
            print('密碼錯誤！ 請等待15秒')
            break
        print('密碼錯誤！ 還有', num, '次機會')