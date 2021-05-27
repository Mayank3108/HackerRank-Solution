n = int(input())
arr= list(map(int, input().split()))
highest = max(arr)
for items in range(n):
    if highest == max(arr):
        arr.remove(max(arr))

print(max(arr))