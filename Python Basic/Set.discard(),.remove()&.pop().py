n = int(input())
s = set(map(int, input().split()))
N=int(input())
i=0
while i < N:
    commands = list(map(str, input().split()))
    if commands[0] == "pop":
        s.pop()
    elif commands[0] == "remove":
        s.remove(int(commands[1]))
    elif commands[0] == "discard":
        s.discard(int(commands[1]))
    i += 1
print(sum(s))
