stroka = str(input())
lenghth = len(stroka)
i = 0
proc = 0
while True:
    if stroka[i] == 'g' or stroka[i] == 'c':
        proc = proc+1
    i=i+1
    if i == int(lenghth):
        otvet = int(proc)/int(lenghth)
        print(otvet*100, '%')
        break;
