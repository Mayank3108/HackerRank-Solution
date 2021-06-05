T = int(input())
i=1
while i <= T:
    a, A = int(input()), set(map(int, input().split()))
    b, B= int(input()), set(map(int, input().split()))
    print(A.issubset(B))
    i += 1
    
