b=0
while True:
    a=int(input('Введите целове число: '))
    if a != 0:
        b=b+a
        continue
    if a == 0:
        print(b)
        break
