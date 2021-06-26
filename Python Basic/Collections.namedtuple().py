# from collections import namedtuple
# n, student = int(input()), namedtuple('student', ",".join(list(map(str, input().strip().split()))))
# print (sum([float(s.MARKS) for s in [student(*input().strip().split()) for _ in range(n)]]) / n)

from collections import namedtuple
n = int(input())
columns  = input().split()
sum = 0

for i in range(n):
    students = namedtuple('student', columns )
    MARKS, CLASS, NAME, ID = input().split()
    student = students(MARKS, CLASS, NAME, ID)
    # sum += int(students.MARKS)
    print(int(students.MARKS))

# print('%.2f'%(sum/n))
