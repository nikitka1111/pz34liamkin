from itertools import cycle
a = list(map(int, input().split()))
c = cycle(a)
res = [next(c) for x in range(len(a)*2+1)][len(a)-1:]
print(a[0] if len(a) == 1 else ' '.join([str(res[x]+res[x+2]) for x in range(len(a))]))
