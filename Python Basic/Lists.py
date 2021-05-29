N = int(input())
i=1
list_ans = []
while i <=N:
    commands = list(map(str,input().split()))
    task = commands[0]
    if task == "insert" :
        list_ans.insert(int(commands[1]), int(commands[2]))
    elif task == "print":
        print(list_ans)
    elif task == "remove":
        list_ans.remove(int(commands[1]))
    elif task == "append":
        list_ans.append(int(commands[1]))
    elif task == "sort":
        list_ans.sort()
    elif task == "pop":
        list_ans.remove(list_ans[-1])
    elif task == "reverse":
        list_ans.reverse()
    i += 1
