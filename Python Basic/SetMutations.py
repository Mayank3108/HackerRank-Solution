n = int (input())
A = set (map(int, input().split()))
N = int (input())
i=0
while i < N:
    command = list(map(str, input().split()))
    if command[0] == "intersection_update":
        ot_set = set(map(int, input().split()))
        A.intersection_update(ot_set)
    elif command[0] == "update":
        ot_set = set(map(int, input().split()))
        A.update(ot_set)
    elif command[0] == "symmetric_difference_update":
        ot_set = set(map(int, input().split()))
        A.symmetric_difference_update(ot_set)
    elif command[0] == "difference_update":
        ot_set = set(map(int, input().split()))
        A.difference_update(ot_set)

    i += 1
print(sum(A))
