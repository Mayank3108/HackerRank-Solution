from itertools import permutations
string, k= input().split()
ans = list(permutations(string,int(k)))
ans.sort()
for i in ans:
    print("".join(i))
    