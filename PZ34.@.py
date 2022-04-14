while True:
    a = int(input('Введите целое число: '))
    if a < 10:
        continue
    elif a > 100:
        break
    else:
        print(a)
