n, m = input().split()
arr = list(map(int, input().split()))
A, B = set(map(int, input().split())), set(map(int, input().split()))
happines = 0 
for element in arr:
    if element in A:
        happines += 1
    elif element in B:
        happines -= 1

print(happines)
 