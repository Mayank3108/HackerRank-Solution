from itertools import combinations_with_replacement
string, k  = input().split()

for j in combinations_with_replacement(sorted(string), int(k)):
    print(''.join(j))