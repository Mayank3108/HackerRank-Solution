from collections import defaultdict
d= defaultdict(list)
n, m = list(map(int, (input().split())))
B=[]
for i in range(0, n):
    d[input()].append(i+1)
for i in range(0, m):
    B.append(input())
for i in B:
    print(*d[B[i]] or [-1])
