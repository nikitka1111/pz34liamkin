a = int(input())
b = int(input())
i = a-1
sum = 0
x=0
while True:
    a=a+1
    if a % 3 == 0:
        x=x+1
        sum = a+sum
    if a == b:
        print(sum/x)
        break;
