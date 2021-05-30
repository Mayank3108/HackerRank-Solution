records=[]
for i in range(int(input())):
        name = input()
        score = float(input())
        records.append([name, score])

records = sorted(records, key = lambda x:x[1])

second_lowest_score = sorted(list(set([x[1] for x in records])))[1]
answer=[]
for ans in records:
    if ans[1] ==second_lowest_score:
        answer.append(ans[0])
print("/n".join(sorted(answer)))

