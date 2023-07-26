i = 0
err_count = 0

while True:
    try:
        num = int(input('input the number:'))
        print(f'You enter a good number {num}')
    except ValueError:
        err_count += 1
        if err_count >= 3:
            print('3 times error, you cannot play')
            break

        print('You should enter the number')

    except KeyboardInterrupt:
        print('Game over')
        break

    finally:
        i += 1
        print(f'You play {i} times')