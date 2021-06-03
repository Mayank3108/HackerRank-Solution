m, M = int(input()), set(map(int, input().split()))
4
n = int(input())
N = set(map(int, input().split()))
for number in sorted(M.symmetric_difference(N)):
    print (number)
