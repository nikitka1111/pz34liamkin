from time import sleep
a = int(input())
b = int(input())
i = max(a,b) - 1
while True:
    i=i+1
    first = i % a
    second = i % b
    print(i)
    sleep(1)
    print('--------------------------')
    print(first)
    print(second)
    print('--------------------------')
    sleep(2)
    if first == 0 and second == 0:
        print(i)
        break
    else:
        continue
