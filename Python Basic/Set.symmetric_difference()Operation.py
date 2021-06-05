m, M = int(input()), set(map(int, input().split()))
n, N = int(input()), set(map(int, input().split()))

for number in sorted(M.symmetric_difference(N)):
    print (number)
