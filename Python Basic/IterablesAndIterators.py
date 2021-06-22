from itertools import combinations
n = int(input())
letters, p, total = input().split(), 0, 0
k = int(input())
for j in combinations(sorted(letters), k):
    total += 1
    if 'a' in j:
        p += 1
print (p/total)
