K, M = list(map(int, input().split()))
i=1
f = []
S=0
while i <= K:
    num = list(map(int, input().split()))
    f.append(max(num))
    i+=1
for element in f:
    S += element**2

print(S%M)
