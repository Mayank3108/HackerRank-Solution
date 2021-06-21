K = int(input())
rooms = list(map(int, input().split()))
myset = set(rooms)

print(((sum(myset)*K)-(sum(rooms)))//(K-1))
